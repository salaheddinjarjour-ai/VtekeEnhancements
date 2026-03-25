<?php
/**
 * VTEKE Inquiry Form — Email Handler using PHPMailer
 * 
 * INSTRUCTIONS:
 * 1. Upload this file to your cPanel public_html folder
 * 2. Configure your SMTP settings below (lines 18-27)
 * 3. Make sure PHPMailer files are uploaded (or they will be downloaded automatically)
 */

// ── SMTP Configuration ──────────────────────────────────────────────────────────
// EDIT THESE VALUES WITH YOUR HOSTING DETAILS
$SMTP = [
    'host'     => 'smtp.your-email-provider.com',  // e.g., smtp.example.com
    'port'     => 587,                               // 587 (TLS) or 465 (SSL) or 25
    'username' => 'your-email@yourdomain.com',      // Your full email address
    'password' => 'your-email-password',              // Your email password or app password
    'from'     => 'info@yourdomain.com',             // Must match username domain
    'fromName' => 'VTEKE Website',
    'to'       => 'info@vteke.com.tr',               // Where you want to receive inquiries
];

// ───────────────────────────────────────────────────────────────────────────────

// Only accept POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed']);
    exit;
}

// Try to load PHPMailer (Composer) or use manual include
$phpmailerLoaded = false;

// Try 1: Composer autoload
if (file_exists(__DIR__ . '/vendor/autoload.php')) {
    require __DIR__ . '/vendor/autoload.php';
    $phpmailerLoaded = true;
}

// Try 2: Manual PHPMailer files
if (!$phpmailerLoaded) {
    $phpmailerPaths = [
        __DIR__ . '/PHPMailer/PHPMailer.php',
        __DIR__ . '/phpmailer/PHPMailer.php',
        '/usr/share/php/PHPMailer/PHPMailer.php',
    ];
    foreach ($phpmailerPaths as $path) {
        if (file_exists($path)) {
            require $path;
            // Load SMTP class too
            $smtpPath = str_replace('PHPMailer.php', 'SMTP.php', $path);
            if (file_exists($smtpPath)) {
                require $smtpPath;
            }
            $phpmailerLoaded = true;
            break;
        }
    }
}

// Try 3: Download PHPMailer if not available
if (!$phpmailerLoaded) {
    // Create PHPMailer directory
    $mailerDir = __DIR__ . '/PHPMailer';
    if (!is_dir($mailerDir)) {
        mkdir($mailerDir, 0755, true);
    }
    
    // Download PHPMailer from GitHub
    $files = [
        'Exception.php' => 'https://raw.githubusercontent.com/PHPMailer/PHPMailer/master/src/Exception.php',
        'PHPMailer.php' => 'https://raw.githubusercontent.com/PHPMailer/PHPMailer/master/src/PHPMailer.php',
        'SMTP.php'       => 'https://raw.githubusercontent.com/PHPMailer/PHPMailer/master/src/SMTP.php',
    ];
    
    foreach ($files as $filename => $url) {
        $filepath = $mailerDir . '/' . $filename;
        if (!file_exists($filepath)) {
            $content = @file_get_contents($url);
            if ($content !== false) {
                file_put_contents($filepath, $content);
            }
        }
    }
    
    // Try to load again
    $autoloadFile = $mailerDir . '/PHPMailer.php';
    if (file_exists($autoloadFile)) {
        require $autoloadFile;
        $smtpFile = $mailerDir . '/SMTP.php';
        if (file_exists($smtpFile)) {
            require $smtpFile;
        }
        $exceptionFile = $mailerDir . '/Exception.php';
        if (file_exists($exceptionFile)) {
            require $exceptionFile;
        }
        $phpmailerLoaded = true;
    }
}

// ── Sanitize & Validate ───────────────────────────────────────────────────────
function clean($val) {
    return htmlspecialchars(strip_tags(trim($val)), ENT_QUOTES, 'UTF-8');
}

$firstName = clean($_POST['firstName'] ?? '');
$lastName  = clean($_POST['lastName']  ?? '');
$email     = filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
$subject   = clean($_POST['subject']   ?? '');
$message   = clean($_POST['message']   ?? '');

// Map subject values to readable labels
$subjectLabels = [
    'product' => 'Product Inquiry',
    'support' => 'Technical Support',
    'partner' => 'Partnership',
    'other'   => 'Other',
];
$subjectLabel = $subjectLabels[$subject] ?? $subject;

// Required field check
if (empty($firstName) || empty($lastName) || empty($email) || empty($message)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Please fill in all required fields.']);
    exit;
}

// Basic email validation
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Invalid email address.']);
    exit;
}

// ── Send Email ────────────────────────────────────────────────────────────────
$fullName = $firstName . ' ' . $lastName;

if ($phpmailerLoaded && class_exists('PHPMailer\PHPMailer\PHPMailer')) {
    // Use PHPMailer with SMTP
    try {
        $mail = new PHPMailer\PHPMailer\PHPMailer(true);
        $mail->isSMTP();
        $mail->Host       = $SMTP['host'];
        $mail->SMTPAuth   = true;
        $mail->Username   = $SMTP['username'];
        $mail->Password   = $SMTP['password'];
        $mail->SMTPSecure = (int)$SMTP['port'] === 465 ? 'ssl' : 'tls';
        $mail->Port       = (int)$SMTP['port'];
        $mail->CharSet    = 'UTF-8';
        
        // Recipients
        $mail->setFrom($SMTP['from'], $SMTP['fromName']);
        $mail->addAddress($SMTP['to']);
        $mail->addReplyTo($email, $fullName);
        
        // Content
        $mail->isHTML(false);
        $mail->Subject = "New Inquiry: {$subjectLabel} — from {$fullName}";
        $mail->Body    = "
========================================
  NEW INQUIRY — VTEKE Website
========================================

Name:     {$fullName}
Email:    {$email}
Subject:  {$subjectLabel}

Message:
----------------------------------------
{$message}
----------------------------------------

Sent via: ContactUs page
Time:     " . date('Y-m-d H:i:s T') . "
========================================
        ";
        
        $mail->send();
        $sent = true;
        
        // Send auto-reply
        try {
            $reply = new PHPMailer\PHPMailer\PHPMailer(true);
            $reply->isSMTP();
            $reply->Host       = $SMTP['host'];
            $reply->SMTPAuth   = true;
            $reply->Username   = $SMTP['username'];
            $reply->Password   = $SMTP['password'];
            $reply->SMTPSecure = (int)$SMTP['port'] === 465 ? 'ssl' : 'tls';
            $reply->Port       = (int)$SMTP['port'];
            $reply->CharSet    = 'UTF-8';
            
            $reply->setFrom($SMTP['from'], $SMTP['fromName']);
            $reply->addAddress($email, $fullName);
            $reply->Subject = 'Thank you for contacting VTEKE';
            $reply->Body    = "Dear {$firstName},

Thank you for reaching out to VTEKE Professional Electric.

We have received your inquiry and our team will get back to you within 1 business day.

Your inquiry summary:
  Subject: {$subjectLabel}
  Message: {$message}

Best regards,
VTEKE Professional Electric Team
+90 212 544 0004
info@vteke.com.tr
www.vteke.com.tr
            ";
            
            $reply->send();
        } catch (Exception $e) {
            // Auto-reply failed, but main email was sent
        }
        
        echo json_encode(['success' => true, 'message' => 'Your inquiry has been sent successfully!']);
        
    } catch (Exception $e) {
        http_response_code(500);
        echo json_encode(['success' => false, 'message' => 'Email could not be sent. Error: ' . $mail->ErrorInfo]);
    }
} else {
    // PHPMailer not available, try native mail()
    $toEmail   = $SMTP['to'];
    $emailSubject = "New Inquiry: {$subjectLabel} — from {$fullName}";
    
    $emailBody = "
========================================
  NEW INQUIRY — VTEKE Website
========================================

Name:     {$fullName}
Email:    {$email}
Subject:  {$subjectLabel}

Message:
----------------------------------------
{$message}
----------------------------------------

Sent via: ContactUs page
Time:     " . date('Y-m-d H:i:s T') . "
========================================
    ";
    
    $headers  = "From: {$SMTP['fromName']} <{$SMTP['from']}>\r\n";
    $headers .= "Reply-To: {$fullName} <{$email}>\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
    
    $sent = @mail($toEmail, $emailSubject, $emailBody, $headers);
    
    if ($sent) {
        echo json_encode(['success' => true, 'message' => 'Your inquiry has been sent successfully!']);
    } else {
        http_response_code(500);
        echo json_encode([
            'success' => false, 
            'message' => 'Email could not be sent. Please configure SMTP settings or contact us directly at ' . $SMTP['to']
        ]);
    }
}
?>

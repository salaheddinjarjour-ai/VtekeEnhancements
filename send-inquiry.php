<?php
// ─────────────────────────────────────────────
//  VTEKE Inquiry Form — Email Handler
//  Sends form submissions to info@vteke.com.tr
// ─────────────────────────────────────────────

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');

// Only accept POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed']);
    exit;
}

// ── Sanitize & Validate ──────────────────────
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

// ── Build Email ──────────────────────────────
$toEmail   = 'info@vteke.com.tr';
$fromName  = 'VTEKE Inquiry Form';
$fullName  = $firstName . ' ' . $lastName;

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

$headers  = "From: {$fromName} <{$toEmail}>\r\n";
$headers .= "Reply-To: {$fullName} <{$email}>\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

// ── Send ─────────────────────────────────────
$sent = mail($toEmail, $emailSubject, $emailBody, $headers);

if ($sent) {
    // Send auto-reply to the visitor
    $replySubject = 'Thank you for contacting VTEKE';
    $replyBody    = "Dear {$firstName},

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
    $replyHeaders  = "From: VTEKE Professional Electric <{$toEmail}>\r\n";
    $replyHeaders .= "Reply-To: {$toEmail}\r\n";
    $replyHeaders .= "Content-Type: text/plain; charset=UTF-8\r\n";
    mail($email, $replySubject, $replyBody, $replyHeaders);

    echo json_encode(['success' => true, 'message' => 'Your inquiry has been sent successfully!']);
} else {
    http_response_code(500);
    echo json_encode(['success' => false, 'message' => 'Could not send email. Please try again or contact us directly at info@vteke.com.tr']);
}
?>

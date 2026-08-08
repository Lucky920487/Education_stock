<?php
// backend/register.php
require 'config.php';
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $conn->real_escape_string($_POST['name'] ?? '');
    $email = $conn->real_escape_string($_POST['email'] ?? '');
    $phone = $conn->real_escape_string($_POST['phone'] ?? '');
    
    // In a real app, they would type their password in the form.
    $raw_password = $_POST['password'] ?? 'default123';
    $password = password_hash($raw_password, PASSWORD_DEFAULT);
    
    // Optional role for testing, default to student
    $role = (isset($_POST['role']) && $_POST['role'] === 'admin') ? 'admin' : 'student';

    if (empty($name) || empty($email)) {
        echo json_encode(["status" => "error", "message" => "Name and email are required."]);
        exit;
    }

    // Check if email exists
    $check = $conn->query("SELECT id FROM users WHERE email = '$email'");
    if ($check->num_rows > 0) {
        echo json_encode(["status" => "error", "message" => "Email already registered."]);
        exit;
    }

    $sql = "INSERT INTO users (name, email, phone, password, role) VALUES ('$name', '$email', '$phone', '$password', '$role')";
    if ($conn->query($sql) === TRUE) {
        echo json_encode(["status" => "success", "message" => "Account created successfully."]);
    } else {
        echo json_encode(["status" => "error", "message" => "Error: " . $conn->error]);
    }
}
?>
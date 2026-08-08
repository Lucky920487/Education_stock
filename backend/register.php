<?php
// backend/register.php
require 'config.php';
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $conn->real_escape_string($_POST['name']);
    $email = $conn->real_escape_string($_POST['email']);
    $phone = $conn->real_escape_string($_POST['phone']);
    $plan = $conn->real_escape_string($_POST['plan']);
    
    // Hash password (we will auto-generate one or accept it from the form)
    // Assuming you add a password field to your form. For now, defaulting:
    $password = isset($_POST['password']) ? password_hash($_POST['password'], PASSWORD_DEFAULT) : password_hash('default123', PASSWORD_DEFAULT);

    // Check if email exists
    $check = $conn->query("SELECT id FROM users WHERE email = '$email'");
    if ($check->num_rows > 0) {
        echo json_encode(["status" => "error", "message" => "Email already registered."]);
        exit;
    }

    $sql = "INSERT INTO users (name, email, phone, plan, password) VALUES ('$name', '$email', '$phone', '$plan', '$password')";
    if ($conn->query($sql) === TRUE) {
        echo json_encode(["status" => "success", "message" => "Account created successfully."]);
    } else {
        echo json_encode(["status" => "error", "message" => "Error: " . $conn->error]);
    }
}
?>
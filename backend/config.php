<?php
// backend/config.php
session_start();

// Handle CORS for local testing if needed
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, GET, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");

if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {
    exit(0);
}

$host = "localhost";
$username = "root"; // Change this on production
$password = ""; // Change this on production
$dbname = "lms_database";

$conn = new mysqli($host, $username, $password, $dbname);

if ($conn->connect_error) {
    header('Content-Type: application/json');
    die(json_encode(["status" => "error", "message" => "Database Connection Failed: " . $conn->connect_error]));
}

// Utility function to verify if user is logged in
function require_login() {
    if (!isset($_SESSION['user_id'])) {
        header('Content-Type: application/json');
        echo json_encode(["status" => "error", "message" => "Unauthorized access."]);
        exit;
    }
}

// Utility function to verify if user is admin
function require_admin() {
    require_login();
    if (!isset($_SESSION['user_role']) || $_SESSION['user_role'] !== 'admin') {
        header('Content-Type: application/json');
        echo json_encode(["status" => "error", "message" => "Forbidden. Admin access required."]);
        exit;
    }
}
?>
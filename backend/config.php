<?php
// backend/config.php
session_start();

$host = "localhost";
$username = "root"; // Change this on production
$password = ""; // Change this on production
$dbname = "lms_database";

$conn = new mysqli($host, $username, $password, $dbname);

if ($conn->connect_error) {
    die(json_encode(["status" => "error", "message" => "Database Connection Failed"]));
}
?>
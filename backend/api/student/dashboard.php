<?php
// backend/api/student/dashboard.php
require '../../config.php';
require_login();
header('Content-Type: application/json');

$user_id = $_SESSION['user_id'];

// Get user profile
$user_query = $conn->query("SELECT name, email, phone, role FROM users WHERE id = $user_id");
$user_data = $user_query->fetch_assoc();

// Get enrolled courses with progress
$courses_query = $conn->query("
    SELECT c.id, c.title, c.thumbnail, c.instructor, e.enrolled_at,
           (SELECT COUNT(l.id) FROM lessons l JOIN modules m ON l.module_id = m.id WHERE m.course_id = c.id) as total_lessons,
           (SELECT COUNT(lp.id) FROM lesson_progress lp JOIN lessons l ON lp.lesson_id = l.id JOIN modules m ON l.module_id = m.id WHERE m.course_id = c.id AND lp.user_id = $user_id) as completed_lessons
    FROM enrollments e
    JOIN courses c ON e.course_id = c.id
    WHERE e.user_id = $user_id
");

$courses = [];
while ($row = $courses_query->fetch_assoc()) {
    $total = (int)$row['total_lessons'];
    $completed = (int)$row['completed_lessons'];
    $row['progress_percentage'] = ($total > 0) ? round(($completed / $total) * 100) : 0;
    $courses[] = $row;
}

// Get stats
$stats = [
    "enrolled_courses" => count($courses),
    "completed_courses" => count(array_filter($courses, function($c) { return $c['progress_percentage'] == 100; })),
    "certificates_earned" => $conn->query("SELECT COUNT(id) as count FROM certificates WHERE user_id = $user_id")->fetch_assoc()['count']
];

echo json_encode([
    "status" => "success",
    "user" => $user_data,
    "courses" => $courses,
    "stats" => $stats
]);
?>
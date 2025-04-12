<?php
// Initialize variables
$file_path = $_GET['file_path'] ?? ''; // Get file path from query string
$file_path = str_replace('../', '', $file_path);
$content = '';
$message = '';
// echo $file_path;

// Validate and process the file path
if (!empty($file_path)) {
    // Ensure the file is within the allowed directory (for security)
    $base_dir = '/var/www/html/';
    $full_path = realpath($base_dir . $file_path);

    // Validate that the file is within the allowed directory

    if (file_exists($full_path)) {
        // Read the content of the file
        $content = file_get_contents($full_path);
    } else {
        $message = 'The story didn\'t exist.';
    }
} else {
    $message = 'Please provide a file path.';
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Read Story</title>
</head>
<body>
    <h1>Read Story</h1>

    <?php if (!empty($message)): ?>
        <p><strong>Message:</strong> <?php echo htmlspecialchars($message); ?></p>
    <?php endif; ?>

    <ul id="menu">              
        <li><a href="/?file_path=content1.txt">Story 1</a></li>
        <li><a href="/?file_path=content2.txt">Story 2</a></li>
        <li><a href="/?file_path=content3.txt">Story 3</a></li>
    </ul>

    <hr>

    <?php if (!empty($content)): ?>
        <h2>Content of Story :</h2>
        <pre><?php echo htmlspecialchars($content); ?></pre>
    <?php endif; ?>
</body>
</html>
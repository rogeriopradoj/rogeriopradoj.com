<?php

$directoryIndexBasepath   = 'index';
$directoryIndexExtensions = ['php', 'html', 'htm'];

function throw404() {
    $statusCode = 404;
    $outputColorRed = ["\033[31m", "\033[37m"];
    file_put_contents(
        "php://stdout",
        sprintf("[%s] %s%s:%s [%s]: %s%s\n",
            date("D M j H:i:s Y"),
            $outputColorRed[0],
            $_SERVER["REMOTE_ADDR"],
            $_SERVER["REMOTE_PORT"],
            $statusCode,
            $_SERVER["REQUEST_URI"],
            $outputColorRed[1]
    ));
    http_response_code($statusCode);
    require $_SERVER["DOCUMENT_ROOT"] . '/' . $statusCode . ".html";
}

// if requesting a directory then serve the default index
$path = parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH);
$ext = pathinfo($path, PATHINFO_EXTENSION);
if (empty($ext)) {
    $path = rtrim($path, "/") . "/" . $directoryIndexBasepath;
}

if (file_exists($_SERVER["DOCUMENT_ROOT"] . $path)) {
    return false;
}  

foreach ($directoryIndexExtensions as $indexExt) {
    if (file_exists($_SERVER["DOCUMENT_ROOT"] . $path . "." . $indexExt)) {
        return false;
    }        
}

throw404();

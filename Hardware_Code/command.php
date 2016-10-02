<?php

if(isset($_GET['command'])) {
	exec('python /home/pi/Desktop/web.py ' . $_GET['command']);
	echo 'Success';
}
else {
	echo 'No command';
}

?>
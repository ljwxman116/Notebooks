<?php
$speed=$_POST["speed"];
$deg=$_POST["deg"];
$out=shell_exec("sh /beta/uv/uv.sh $speed $deg");
echo $out;
?>

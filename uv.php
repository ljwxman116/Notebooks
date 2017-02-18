<?php
$speed=$_POST["speed"];
$deg=$_POST["deg"];
$out=shell_exec("sh /beta/bkg/pic.sh $speed $deg");
echo $out;
?>

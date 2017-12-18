<?php
  $host = "localhost";
  $user = "root";
  $pw = "tjddlr072rp";
  $dbName = "myservice";

  if($this->dbConnection == null){
    $this->dbConnection = new mysqli($host, $user, $pw, $dbName);
    $this->dbConnection->set_charset("utf8");
  }
?>

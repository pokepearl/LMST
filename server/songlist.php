<html lang="en">
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

</style>
<title>Example - LMST</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="description" content="">
<meta name="author" content="">
<!-- Bootstrap core CSS -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
</head>
<body>
<!--Ignore the below php section, this imports the header file for the navbar -->
<?php
include 'header.php';
include 'config.php';
?>
<main role="main" class="container mx-auto">
<!-- This Section is Centred, place your code in here -->
<br>
<br>
<br>
<div class="Track-Table">
	<table style="width:100%" class="table">
		<thead>
		<tr>
		<th>ID:</th>
		<th>Title:</th>
		<th>Artist:</th>
		<th>Album:</th>
		<th>Length:</th>
		</tr>
		</thead>
<?php
$results = $db->query('SELECT * FROM song ORDER BY id');
while ($row = $results->fetchArray()) {
// Properly Join Tables to allow reading from Album Tables for Link
	echo "<tr><td>". $row['id'] ."</td><td><a href='songinfo.php?id=". $row['id']."'>". $row['title'] ."</a></td><td>". $row['artist'] ."</td><td><a href='albuminfo.php?id=". urlencode($row['album']) ."'>". $row['album'] ."</a></td><td>". $row['length'] ."</td></tr>";
}
?>
<!--      <tr>
    <td>Placeholder</td> 
    <td>Placeholder</td>
	<td>Placeholder</td> 
    <td>Placeholder</td>
  </tr>-->
</table>
</div>

</main>
<!-- Bootstrap 4 JS Files -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
</body>
</html>
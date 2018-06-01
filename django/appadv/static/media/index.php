<?php
include 'config.php';

//把文章取出来
$sql="SELECT * FROM page ORDER BY pid DESC  Limit 0,10";
$result=$db->query($sql);
$blogs=array();
while ($blog=$result->fetch_assoc()){
    $blogs[]=$blog;
}


//定义每页显示的数量
$pageNum=$setting['pagenum'];

//获取并处理当前页码   ！！分页效果可以做成一个类
$page=(int)$input->get('page');
$page=$page<1?1:$page;
$offset=($page-1)*$pageNum;

//查询显示的显示每页的数量及数据
$rows=array();
$sql="SELECT * FROM page ORDER BY pid DESC LIMIT {$offset},{$pageNum}";
$result=$db->query($sql);
while ($row=$result->fetch_assoc()){
    $rows[]=$row;
}

//查询数据行数并且计算显示页数
$sql="SELECT COUNT(*) AS total FROM page";
$total=$db->query($sql)->fetch_assoc();
$total=(int)$total['total'];
$total=(int)ceil($total/$pageNum);
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="bookmark" type="image/x-icon" href="themes/img/favicon.ico" />
    <link rel="shortcut icon" href="themes/img/favicon.ico">
    <title><?php echo $setting['title'] ?></title>
    <script src="themes/jquery-3.1.1.js" type="text/javascript" charset="utf-8"></script>
    <link rel="stylesheet" type="text/css" href="themes/bootstrap-3.3.7-dist/css/bootstrap.css" />
    <script src="themes/bootstrap-3.3.7-dist/js/bootstrap.js" type="text/javascript" charset="utf-8"></script>
</head>
<body>
    <div class="container">
    	<div class="jumbotron">
    	    <h1><?php echo $setting['title'] ?></h1>
    	    <p><?php echo $setting['intro'] ?></p>
    	    <p><a class="btn btn-info btn-lg" href="admin/login.php" role="button">后台管理</a></p>
    	</div>
	<div class="col-md-3">
		<div class="panel panel-info">
		  <div class="panel-heading">Panel heading without title</div>
		  <div class="panel-body">
		    Panel content
		  </div>
		</div>
		<div class="panel panel-info">
		  <div class="panel-heading">Panel heading without title</div>
		  <div class="panel-body">
		    Panel content
		  </div>
		</div>
	</div>
	<div class="col-md-9">
		<?php foreach ($blogs as $blog):?>
		<div class="panel panel-warning">
		  <div class="panel-heading">
             <a href="web/read.php?pid=<?php echo $blog['pid'];?>"><?php echo $blog['title'];?></a>
          </div>
		  <div class="panel-body">
		    <?php echo mb_substr(strip_tags($blog['content']),0,150)?>
		  </div>
		</div>
        <?php endforeach;?>
        <!--分页-->
        <nav aria-label="Page navigation"  class="pull-right">
            <ul class="pagination">
                <li>
                    <a href="#" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                </li>

                <?php
                $hrefTpl='<li><a href="index.php?page=%d">%s</a></li>';
                for($i=1;$i<=$total;$i++){
                    echo sprintf($hrefTpl,$i,$i);
                }
                ?>
                <li>
                    <a href="#" aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>
            </ul>
        </nav>
	</div>

</body>

</html>
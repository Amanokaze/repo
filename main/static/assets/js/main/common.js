$.ajax({
    type: "GET",
    url: "/main/sidebar-games/",
    success: sidebar_games_result,
    dataType: 'html'
});        

function sidebar_games_result(data, textStatus, jqXHR)
{
	$('#sidebar-games').html(data);
}

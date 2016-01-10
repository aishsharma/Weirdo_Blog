//Starts the Sammy app on page load
$(function() {
	app.run("#/");
});

//Any app config or constant variables go here
var config = {
    //Location of views/templates that are loaded into browser when user visits site
	VIEWS: "views/",
    
    //circle spinner gif that is displayed when page data is being retrieved from server
	LOADSPINNER: "<div id='spinner'><i class='fa fa-spinner fa-pulse fa-5x'></i></div>"
};


//App Routes go here
var app = $.sammy("#content", function() {
	//Home Page
	this.get("#/", function(context) {
		Blog.loadContent("main.html");
	});
});

var Blog = Blog || {};

//Loads content from a file in views folder
Blog.loadContent = function(file) {

	//Showing a load spinner till all ajax is completed	
	$("#content").html(config.LOADSPINNER);

	//Will hold view data
	var view;

	//Getting template
	$.get(config.VIEWS + file, function(html) {
			templateHtml = html;
		}, "html")
		.done(function() {
			$("#content").html(templateHtml);
		})
		.fail(function() {});
};
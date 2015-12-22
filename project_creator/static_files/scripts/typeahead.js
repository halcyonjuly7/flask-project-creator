
$(function(){
	$("#typeahead").typeahead({
		items: 4, 
		source: function(query, process){
			console.log(query)
			$.ajax({
				url:"route_here",
				type: "POST",
				data: JSON.stringify({"data":query}),
				contentType:"application/json;charset=UTF-8",
				success: function(data) {
					
					process(data["jobs"])
				}


			});
		}
	});	
})
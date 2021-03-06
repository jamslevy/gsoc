$(document).ready(function() {
	$("#applications_progress_bar").progressBar({showText: false});
});

function bulkReviewInit(bulk_review_link,button) {
	// get the JSON object with details of every application for bulk acceptance
	$.getJSON(bulk_review_link+"?_="+(new Date().getTime()),
		function(data){
			// If there are applications to review...
			if (data.nr_applications != 0) {
				//...then fade out the button, show the progress bar and call the function for review
				$("[id^=button_bulk_]").fadeOut("slow",
					function() {
						$("#applications_progress_bar").progressBar(0);
						$("#description_done").html("");
						$("#applications_progress_bar").fadeIn("slow", bulkReview(data));
					}
				);
			}else {
				var no_organization_text="No organizations to ";
				if ($(button).attr("id").indexOf("reject")!=-1) {
					no_organization_text+="reject";
				}
				else {
					no_organization_text+="accept";
				}
				$("#description_done").html("<strong>"+no_organization_text+"</strong>");
			}
		}
	);
}

function bulkReview(data) {
	// some global constants
	var GLOBAL_LINK = data.link;
	var TOTAL_APPLICATIONS = data.nr_applications;

	// some global variables set needed for internal iteration
	var application_index = 0;
	// number of iteration is not taken from data.nr_applications
	// to ensure avoidance of array out of bounds errors
	var total_index = data.applications.length;


	// call immediately the function for review
	// real iteration is inside
	setTimeout(function(){
		var error_happened = false;

		var application = data.applications[application_index];
		var current_application = application_index + 1;
		// regular expression to find a valid scope path inside matching parenthesis
		var re = /\((\w*)\)/;
		var scope_path = GLOBAL_LINK.match(re)[1];
		// the URL is obtained by using the scope path found in the matching parenthesis
		var url_to_call = GLOBAL_LINK.replace(re, eval("application." + scope_path));
		// now we can call the URL found
		$.ajax({
			async: false,
			cache: false,
			url: url_to_call,
			timeout: 10000,
			success: function(data) {
				if (data) {
					// update progress bar percentage and description
					var percentage = Math.floor(100 * (current_application) / (TOTAL_APPLICATIONS));
					$("#description_progressbar").html(" Processed application " + application.name + " (" + (current_application) + "/" + TOTAL_APPLICATIONS + ")");
					$("#applications_progress_bar").progressBar(percentage);
				}
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) {
				// if there is an error return the button and leave a try again message
				error_happened = true;
				$("[id^=button_bulk_]").fadeIn("slow", function() {
					$("#description_done").html("<strong class='error'> Error encountered, try again</strong>");
				});
			}
		});
		// if there were no errors, continue the iteration
		if (!error_happened) {
			// prepare for new iteration and then recall this function
			application_index++;
			if (application_index < total_index) {
				setTimeout(arguments.callee, 0);
			}
			else {
				// all ok, tell the user we are done
				$("#applications_progress_bar").fadeOut("slow",
					function() {
						$("#applications_progress_bar").progressBar(0);
						$("[id^=button_bulk_]").fadeIn("slow");
					}
				);
				$("#description_progressbar").html("");
				$("#description_done").html("<strong>Done!</strong>");
			}
		}
	},0);
}

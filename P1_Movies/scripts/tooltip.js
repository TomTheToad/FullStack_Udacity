/*
 * 	JavaScript
 * 	written by Victor Asselta
 * 	originally adapted from a script/ online course
 * 	created by Chris Converse for Lynda.com.
 * 
 * 	version 1.0
 * 	A tooltip script which allows for the creation
 * 	of mouseOver tool tip windows.
 */

$(document).ready(function() {
	
	$('.TooltipMouseOver').mouseover(function(e) {
		
		// HTML for mouseOver Tooltip
		if ( $(this).attr('data-tip-type') == 'html' ){
			var elementToGet = '#' + $(this).attr('data-tip-source');
			var newHTML = $(elementToGet).html();
			$('#tooltipContainer').html( newHTML );
		}
		
		$('#tooltipContainer').css('display','block');
		
	}).mousemove(function(e) {
		
		// Resizes or repositions the tooltip window as necessary
		var tooltipWidth = $('#tooltipContainer').outerWidth();
		var tooltipHeight = $('#tooltipContainer').outerHeight();
		
		var pageWidth = $('body').width();
		if(e.pageX > pageWidth/2) {
			$('#tooltipContainer').css('left',(e.pageX-tooltipWidth+20)+'px');
		} else {
			$('#tooltipContainer').css('left', (e.pageX-20)+'px');
		}
		
		var pageHeight = $('body').height();
		if(e.pageY > (pageHeight/2)){
			$('#tooltipContainer').css('top', (e.pageY-tooltipHeight-30)+'px');
		} else {
			$('#tooltipContainer').css('top', (e.pageY+30)+'px');
		}
		

	}).mouseout(function(e) {

		// Hides the tooltip window if mouse is moved from target
		$('#tooltipContainer').css('display','none').html('');

		// Hides the tooltip window if mouse is clicked.
		}).click(function(e){
		$('#tooltipContainer').css('display','none').html('');
	});
});

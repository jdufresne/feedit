(function($) {
	$(document).ready(function() {
		$('.entry').find('form').hide();
	});

	$(document).on('click', '.entry', function() {
		$('.active').removeClass('active');
		var self = $(this);
		self.addClass('active');
		var form = self.find('form');
		$.ajax(form.attr('action'), {
			'type': 'POST',
			'dataType': 'json',
			'data': form.serializeArray()
		});
	});
})(jQuery);

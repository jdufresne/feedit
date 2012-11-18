(function($) {
	$(document).ready(function() {
		$('.entry').find('form').hide();

		$(document).on('click', '.entry', function() {
			readEntry(this);
		});

		var SCROLL_THRESHOLD = 30;
		$(window).scroll(function() {
			scroll = $(this).scrollTop()
			$('.entry').each(function() {
				var diff = $(this).offset().top - scroll;
				if (Math.abs(diff) < SCROLL_THRESHOLD)
				{
					readEntry(this);
				}
			});
		});
	});

	function readEntry(el) {
		el = $(el);
		$('.active').removeClass('active');
		el.addClass('active');
		if (!el.is('.read'))
		{
			el.addClass('read');
            // Form will not exist for anonymous user
            var form = el.find('form');
            if (form.length)
            {
			    submitAjax(form);
            }
		}
	}

	function submitAjax(el) {
		el = $(el).closest('form');
		$.ajax(el.attr('action'), {
			'type': el.attr('method'),
			'dataType': 'json',
			'data': el.serialize()
		});
	}
})(jQuery);

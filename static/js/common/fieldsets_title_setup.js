$(document).ready(function(jQuery) {
    jQuery(function($) {
        if (window.location.href.indexOf("/change/") !== -1 || window.location.href.indexOf("/add/") !== -1) {
            $("h2.fieldset-heading").removeTitleText();
        }
    });
});

(function($) {
    $.fn.removeTitleText = function() {
        this.filter("h2.fieldset-heading").each(function() {
            var $this = $(this);
            var newText = $this.text().replace("title ", "");
            $this.text(newText);
        });
        return this;
    };
})(jQuery);
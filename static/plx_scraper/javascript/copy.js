$(".copy-btn").click(function() {
    let tmpElement = $('<textarea style="opacity:0;"></textarea>');
    let parent = $(this).closest('td').siblings().each(function(){
        tmpElement.text(tmpElement.text() + $(this).text() + '\t');
    });
    
    tmpElement.appendTo($('body')).focus().select();
    document.execCommand("copy");
    tmpElement.remove();
});

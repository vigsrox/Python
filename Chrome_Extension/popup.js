document.addEventListener('DOMContentLoaded', function() {
  var genpwdButton = document.getElementById('bt_Generate_Password');
    genpwdButton.addEventListener('click', function() {
    chrome.tabs.getSelected(null, function(tab) {
       document.getElementById("tf_Website").value = tab.url;
    });
  }, false);

}, false);
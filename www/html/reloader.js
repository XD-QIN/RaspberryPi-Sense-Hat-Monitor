function reloadGraph() {
   var now = new Date();

   document.images['graph'].src = 'temp_history.svg?' + now.getTime();

   // Start new timer (1 min)
   timeoutID = setTimeout('reloadGraph()', 1000);
}
global_namespace.Define('data-free.startpad.org', function(NS) {

NS.Extend(NS, {
	sCSRF: "",
	apikey: undefined,

Init: function(sCSRF)
	{
	NS.sCSRF = sCSRF;
	}	
});});

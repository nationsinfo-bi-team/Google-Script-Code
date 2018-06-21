function autokena(){
    var MILLIS_PER_DAY = 1000 * 60 * 60 * 24
  var date=new Date()
  var yesterday = new Date(date.getTime() - MILLIS_PER_DAY)
  yesterday=Utilities.formatDate(yesterday,"PST","yyyy-MM-dd")
  //gettoken
    var pay =          
      '<?xml version="1.0" encoding="utf-8"?>'
      +'<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
        +'<soap:Body>'
         +'<clientLogin xmlns="https://advertising.criteo.com/API/v201305">'
          +"<username>echanez@nationsinfocorp.com</username>"
          +"<password>goNat10ns!</password>"
          +"<source>''</source>"
         +"</clientLogin>"
        +"</soap:Body>"
       +"</soap:Envelope>"
       
       
       
       
       
       

    var options =
      {
        "method" : "post",
        "contentType" : "text/xml; charset=utf-8",
        "Content-Length":"length",
        "payload": pay,
        "muteHttpExceptions":true,
        "SOAPAction": '"https://advertising.criteo.com/API/v201305/clientLogin"'
      };
  
  var result = UrlFetchApp.fetch("https://advertising.criteo.com/API/v201305/AdvertiserService.asmx?WSDL", options);
  var dsheet=SpreadsheetApp.openByUrl('https://docs.google.com/spreadsheets/d/1Jlov5n-Yunm7Eyz573PFPl1rt8mlKGY_MMMDwVag2Fo/edit#gid=0')
  var aut = XmlService.parse(result).getRootElement().getChildren()[0].getChildren()[0].getChildren()[0].getText()

  //get jobid
    var pay =          
      '<?xml version="1.0" encoding="utf-8"?>'
    +'<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
      +'<soap:Header>'
      +'<apiHeader xmlns="https://advertising.criteo.com/API/v201305">'
     +'<authToken>'+aut+'</authToken>'
      +'<appToken>7546791053888090112</appToken>'
      +'<clientVersion>?</clientVersion>'
   + '</apiHeader>'
  +'</soap:Header>'
  +'<soap:Body>'
   +'<scheduleReportJob xmlns="https://advertising.criteo.com/API/v201305">'
      +'<reportJob>'
        +'<selectedColumns>'
          +'<ReportColumn>cost</ReportColumn>'
        +'</selectedColumns>'
        +'<reportSelector>'
        +'</reportSelector>'
       +'<reportType>Campaign</reportType>'
        +'<aggregationType>Daily</aggregationType>'
        +'<startDate>'+yesterday+'</startDate>'
        +'<endDate>'+yesterday+'</endDate>'
        +'<isResultGzipped>false</isResultGzipped>'
      +'</reportJob>'
       +'</scheduleReportJob>'
        +"</soap:Body>"
       +"</soap:Envelope>"
  

    var options =
      {
        "method" : "post",
        "contentType" : "text/xml; charset=utf-8",
        "Content-Length":"length",
        "payload": pay,
        "muteHttpExceptions":true,
        "SOAPAction": '"https://advertising.criteo.com/API/v201305/scheduleReportJob"'
      };
  var result = UrlFetchApp.fetch("https://advertising.criteo.com/API/v201305/AdvertiserService.asmx?WSDL", options);
  var dsheet=SpreadsheetApp.openByUrl('https://docs.google.com/spreadsheets/d/1Jlov5n-Yunm7Eyz573PFPl1rt8mlKGY_MMMDwVag2Fo/edit#gid=0')
  var job = XmlService.parse(result).getRootElement().getChildren()[0].getChildren()[0].getChildren()[0].getChildren()[0].getText()

  
  //getdownloadlink
 var pay =          
      '<?xml version="1.0" encoding="utf-8"?>'
    +'<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
      +'<soap:Header>'
      +'<apiHeader xmlns="https://advertising.criteo.com/API/v201305">'
     +'<authToken>'+aut+'</authToken>'
      +'<appToken>7546791053888090112</appToken>'
      +'<clientVersion>?</clientVersion>'
   + '</apiHeader>'
  +'</soap:Header>'
  +'<soap:Body>'
   +'<getReportDownloadUrl xmlns="https://advertising.criteo.com/API/v201305">'
      +'<jobID>'+job+'</jobID>'
    +'</getReportDownloadUrl>'
     +"</soap:Body>"
       +"</soap:Envelope>"
       
    var options =
      {
        "method" : "post",
        "contentType" : "text/xml; charset=utf-8",
        "Content-Length":"length",
        "payload": pay,
        "muteHttpExceptions":true,
        "SOAPAction": '"https://advertising.criteo.com/API/v201305/getReportDownloadUrl"'
      };
  var result = UrlFetchApp.fetch("https://advertising.criteo.com/API/v201305/AdvertiserService.asmx?WSDL", options);
  var dsheet=SpreadsheetApp.openByUrl('https://docs.google.com/spreadsheets/d/1Jlov5n-Yunm7Eyz573PFPl1rt8mlKGY_MMMDwVag2Fo/edit#gid=0')
  var dllink = XmlService.parse(result).getRootElement().getChildren()[0].getChildren()[0].getChildren()[0].getText()
 
 
  dsheet.getSheetByName("Criteo").getRange('b1').setValue(dllink)
  
}

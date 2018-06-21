function myFunction() {
  var now = new Date();
  var ss = SpreadsheetApp.openById("1bL0UxJkuPVSyqcAT3pNbc4oSUt5h4veY7iis6JFLRu4")
  var s1=ss.getSheetByName("Processor Transaction")
  var rcheck1=s1.getRange("J6").getCell(1,1).getValue()
  var rcheck=s1.getRange("J7").getCell(1,1).getValue()
  if(rcheck1>0){
    GmailApp.sendEmail("shutingz@nationsinfocorp.com", "Sale Amount Alert", "check Processor: "+rcheck);
    GmailApp.sendEmail("zhongxingz@nationsinfocorp.com", "Sale Amount Alert", "check Processor: "+rcheck);
    GmailApp.sendEmail("james.diaz@nationsinfocorp.com", "Sale Amount Alert", "check Processor: "+rcheck);
    GmailApp.sendEmail("dorothyc@nationsinfocorp.com", "Sale Amount Alert", "check Processor: "+rcheck);
}
}

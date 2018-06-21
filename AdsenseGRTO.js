function adClients() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('AdClients');
  var clients = AdSense.Adclients.list().getItems();
  for (var i=0; i<clients.length; i++) {
    sheet.getRange('A' + String(i+2)).setValue(clients[i].getId());
    sheet.getRange('B' + String(i+2)).setValue(clients[i].getProductCode());
  }
}
function daildy() {
  var ss = SpreadsheetApp.openByUrl('https://docs.google.com/spreadsheets/d/1lakSeK1QVvaOD7776QPgPWV7e74Lp08zKgOP0GsVBas/edit#gid=0');
  var sheet = ss.getSheetByName('View');
  var today = new Date();
  var timezone = Session.getTimeZone();
  var yesterday = new Date(today.getTime() -  24 * 60 * 60 * 1000);
  var startDate = Utilities.formatDate(yesterday, timezone, 'yyyy-MM-dd');
  var endDate = Utilities.formatDate(yesterday, timezone, 'yyyy-MM-dd');
  var adClientId = "ca-pub-7355929733360605";
  var args = {
    'filter': ['AD_CLIENT_ID==' + adClientId],
    'metric': ['MATCHED_AD_REQUESTS', 'CLICKS', 
               'EARNINGS'],
    'dimension': ['Date']};
  var report = AdSense.Accounts.Reports.generate('pub-7355929733360605',startDate, endDate, args).getRows();
  for (var i=0; i<report.length; i++) {
    var row = report[i];
    row[4]="GRTO";
    sheet.appendRow(row)
  }
}
function generateReport() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('Reports');
  var startDate = Browser.inputBox("Enter a start date (format: 'yyyy-mm-dd')");
  var endDate = Browser.inputBox("Enter an end date (format: 'yyyy-mm-dd')");
  var adClientId = Browser.inputBox("Enter an ad client id");
  var args = {
    'filter': ['AD_CLIENT_ID==' + adClientId],
    'metric': ['PAGE_VIEWS', 'AD_REQUESTS', 'MATCHED_AD_REQUESTS',
               'INDIVIDUAL_AD_IMPRESSIONS'],
    'dimension': ['MONTH']};
  var report = AdSense.Reports.generate(startDate, endDate, args).getRows();
  for (var i=0; i<report.length; i++) {
    var row = report[i];
    sheet.getRange('A' + String(i+2)).setValue(row[0]);
    sheet.getRange('B' + String(i+2)).setValue(row[1]);
    sheet.getRange('C' + String(i+2)).setValue(row[2]);
    sheet.getRange('D' + String(i+2)).setValue(row[3]);
    sheet.getRange('E' + String(i+2)).setValue(row[4]);
  }
}

# Google-Script-Code

function dailyreport() {
  var ss = SpreadsheetApp.openByUrl('https://docs.google.com/spreadsheets/d/1pWZUHgiOzy-0hnGN3NQOdcrBmaGqKlp07USXHNIvf6I/edit#gid=0');
  var sheet = ss.getSheetByName('Reports');
  var today = new Date();
  var timezone = Session.getTimeZone();
  var yesterday = new Date(today.getTime() -  24 * 60 * 60 * 1000);
  var startDate = Utilities.formatDate(yesterday, timezone, 'yyyy-MM-dd');
  var endDate = Utilities.formatDate(yesterday, timezone, 'yyyy-MM-dd');
  var adClientId = "ca-pub-8345955657485355";
  var args = {
    'filter': ['AD_CLIENT_ID==' + adClientId],
    'metric': ['MATCHED_AD_REQUESTS', 'CLICKS', 
               'EARNINGS'],
    'dimension': ['AD_UNIT_NAME']};
  var report = AdSense.Accounts.Reports.generate('pub-8345955657485355',startDate, endDate, args).getRows();

  for (var i=0; i<report.length; i++) {
    var row = report[i];
    row[4]=yesterday;
    sheet.appendRow(row)
  }
}

function adClients() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('AdClients');
  var clients = AdSense.Adclients.list().getItems();
  for (var i=0; i<clients.length; i++) {
    sheet.getRange('A' + String(i+2)).setValue(clients[i].getId());
    sheet.getRange('B' + String(i+2)).setValue(clients[i].getProductCode());
  }
}

function daily() {
  var ss = SpreadsheetApp.openByUrl('https://docs.google.com/spreadsheets/d/1lakSeK1QVvaOD7776QPgPWV7e74Lp08zKgOP0GsVBas/edit#gid=0');
  var sheet = ss.getSheetByName('View');
  var today = new Date();
  var timezone = Session.getTimeZone();
  var yesterday = new Date(today.getTime() -  24 * 60 * 60 * 1000);
  var startDate = Utilities.formatDate(yesterday, timezone, 'yyyy-MM-dd');
  var endDate = Utilities.formatDate(yesterday, timezone, 'yyyy-MM-dd');
  var adClientId = "ca-pub-8345955657485355";
  var args = {
    'filter': ['AD_CLIENT_ID==' + adClientId],
    'metric': ['MATCHED_AD_REQUESTS', 'CLICKS', 
               'EARNINGS'],
    'dimension': ['Date']};
  var report = AdSense.Accounts.Reports.generate('pub-8345955657485355',startDate, endDate, args).getRows();
  for (var i=0; i<report.length; i++) {
    var row = report[i];
    row[4]="RS";
    sheet.appendRow(row)
  }
}


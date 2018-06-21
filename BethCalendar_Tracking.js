function myFunction() {
  var d=new Date("05/06/2017")
  var e=new Date()
  e.setDate(e.getDate()+14)
  var a=CalendarApp.getCalendarById("bethu@nationsinfocorp.com").getEvents(d,e)
  var url="https://docs.google.com/spreadsheets/d/1a4dS-LHCwOaXhTZ60ry4EW1ym4sOOts6BFWUXh3GrPQ/"
 for (i=0;i<a.length;i++)
 {
   SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/1a4dS-LHCwOaXhTZ60ry4EW1ym4sOOts6BFWUXh3GrPQ/").getSheetByName("Calendar_Scrape").getRange(i+1, 1).setValue(a[i].getTitle())
   SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/1a4dS-LHCwOaXhTZ60ry4EW1ym4sOOts6BFWUXh3GrPQ/").getSheetByName("Calendar_Scrape").getRange(i+1, 2).setValue(a[i].getStartTime())
    }
}


function myFunction() {
  var d=new Date("05/01/2018")
  var e=new Date("05/30/2018")
  
  var a=CalendarApp.getCalendarById("nationsinfocorp.com_ihjtujdlr5vcl1u1k7iq9mtmak@group.calendar.google.com").getEvents(d,e)
  var url="https://docs.google.com/spreadsheets/d/1BGoEz_IICl1DweyN6IeCuBynoIm6lalcyoED6ZGf7TU"
 for (i=0;i<a.length;i++)
 {
   SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/1BGoEz_IICl1DweyN6IeCuBynoIm6lalcyoED6ZGf7TU/").getSheetByName("Raw").getRange(i+1, 1).setValue(a[i].getTitle())
 SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/1BGoEz_IICl1DweyN6IeCuBynoIm6lalcyoED6ZGf7TU/").getSheetByName("Raw").getRange(i+1, 2).setValue(a[i].getStartTime())
    SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/1BGoEz_IICl1DweyN6IeCuBynoIm6lalcyoED6ZGf7TU/").getSheetByName("Raw").getRange(i+1, 3).setValue(a[i].getCreators())
 }
}

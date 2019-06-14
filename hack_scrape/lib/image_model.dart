class ListItem{
  int id;
  String title,description,prize,date,skills,url;

  ListItem(this.id,this.title,this.description,this.date,this.skills,this.prize,this.url);

  ListItem.fromJson(parsedJson){
    id=parsedJson["ID"];
    description=parsedJson["Description"];
    prize=parsedJson["Prize Money"];
    date=parsedJson["Date"];
    title=parsedJson["Title"];
    skills=parsedJson["Skills"];
    url=parsedJson["URL"];
  }
}
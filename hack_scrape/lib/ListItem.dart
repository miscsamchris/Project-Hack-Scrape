import 'package:flutter/material.dart';
import 'image_model.dart';
import 'package:url_launcher/url_launcher.dart';
class ItemList extends StatelessWidget{
  final List<ListItem> images;
  ItemList(this.images);


  Widget build(context){
    return ListView.builder(
      itemCount: images.length,
      itemBuilder: (context,int index){
        return buildImage(images[index]);
      },
    );
  }

  Widget buildImage(ListItem image){
    return GestureDetector(
      onDoubleTap: (){
        _launchURL(image.url);
      },
      child: Container(
      padding: EdgeInsets.all(20.0),
      decoration: BoxDecoration(
          border: Border.all(
              color: Colors.lightGreen,
          ),
      ),
      margin: EdgeInsets.all(20.0),
      child: Column(
        children: <Widget>[
          Text(image.title,
            style: TextStyle(
              fontSize: 20.0,
              fontWeight: FontWeight.bold,
              color: Colors.green,
            ),
            textAlign: TextAlign.center,
          ),
          Container(margin: EdgeInsets.only(bottom: 25.0),),
          Text(image.description,
            style: TextStyle(
            fontSize: 10.0,
            fontWeight: FontWeight.bold,
            color: Colors.green,
          ),
      textAlign: TextAlign.justify,
          ),
          Container(margin: EdgeInsets.only(bottom: 25.0),),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: <Widget>[
              Text(image.date,
                style: TextStyle(
                  fontSize: 15.0,
                  fontWeight: FontWeight.bold,
                  color: Colors.green,
                ),
                textAlign: TextAlign.left,
              ),
              Text(image.prize,
                style: TextStyle(
                  fontSize: 15.0,
                  fontWeight: FontWeight.bold,
                  color: Colors.green,
                ),
                textAlign: TextAlign.right,
              ),
            ],
          ),
          Container(margin: EdgeInsets.only(bottom: 25.0),),
          Text(image.skills,
            style: TextStyle(
              fontSize: 20.0,
              fontWeight: FontWeight.bold,
              color: Colors.green,
            ),
            textAlign: TextAlign.center,
          ),
        ],
      ),
    ),
    );
  }
  _launchURL(String link) async {
    var url = link;
    if (await canLaunch(url)) {
      await launch(url);
    } else {
      throw 'Could not launch $url';
    }
  }
}
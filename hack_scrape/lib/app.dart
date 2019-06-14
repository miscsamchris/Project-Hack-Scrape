import 'package:flutter/material.dart';
import 'package:http/http.dart' show get;
import 'image_model.dart';
import 'dart:convert';
import 'ListItem.dart';
class App extends StatefulWidget{
  createState() {
    return AppState();
  }
}
class AppState extends State<App>{
  int counter=0;
  List<ListItem> images=[];
  void fetchImage() async{
    images=[];
      counter++;
      var response = await get(
          "http://192.168.0.104:5000/");
      var jsoninp=json.decode(response.body);
      for(var i in jsoninp){
        var li = new ListItem.fromJson(i);
        setState(() {
          images.add(li);
        });
      }
  }
  Widget build(context){
    var app = MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.black,
        body: ItemList(images),
        floatingActionButton: FloatingActionButton(onPressed: fetchImage,
          child: Icon( Icons.autorenew,
          color: Colors.black,
          ),
          backgroundColor:Colors.green,
        ),
        appBar: AppBar(
          title: Text("Hackathons",
          style: TextStyle(
            color: Colors.black,
          ),
          ),
          backgroundColor: Colors.green,
        ),
      ),
    );
    return app;
  }
}
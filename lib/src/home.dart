import 'package:Eevee/src/StudyMode.dart';
import 'package:flutter/material.dart';

class MyHome extends StatefulWidget {
  const MyHome({Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() {
    return _MyHome();
  }
}

class _MyHome extends State<MyHome> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: const Text('Welcome to Eevee'),
        actions: <Widget>[
          IconButton(
            icon: const Icon(Icons.add_alert),
            tooltip: 'Show Snackbar',
            onPressed: () {
              ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('This is a snackbar')));
            },
          ),
          IconButton(
            icon: const Icon(Icons.navigate_next),
            tooltip: 'Enter Study Mode',
            onPressed: () {
              Navigator.push(context, MaterialPageRoute<void>(
                builder: (BuildContext context) {
                  return const StudyMode();
                },
              ));
            },
          ),
        ],
      ),
      body: Container(
        height: MediaQuery.of(context).size.height,
        width: MediaQuery.of(context).size.width,
        margin: const EdgeInsets.all(10.0),
        child: Container(
          color: Colors.blue,
          child: Center(
            child: Card(
              color: Colors.white,
              elevation: 10.0,
              child: SizedBox(
                  width: 175.0,
                  height: 175.0,
                  child: Image.asset('assets/images/eevee_logo.jpg')),
            ),
          ),
        ),
      ),
    );
  }

  void onPressed() {
    print("Pressed");
  }
}

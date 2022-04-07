import 'package:flutter/material.dart';

class StudyMode extends StatefulWidget {
  const StudyMode({Key? key}) : super(key: key);

  @override
  State<StudyMode> createState() => _StudyModeState();
}

class _StudyModeState extends State<StudyMode> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Study Mode'),
      ),
      body: const Center(
        child: Text(
          "Study Mode",
          style: TextStyle(fontSize: 24),
        ),
      ),
    );
  }
}

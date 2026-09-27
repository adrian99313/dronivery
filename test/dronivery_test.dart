import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:dronivery/main.dart';

void main() {
  testWidgets('Home page renders Dronivery application', (WidgetTester tester) async {
    tester.view.physicalSize = const Size(1280, 900);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.resetPhysicalSize);

    await tester.pumpWidget(const MyApp());
    await tester.pumpAndSettle();

    // Verify title text exists in app bar / branding
    expect(find.text('dronivery'), findsOneWidget);
  });
}

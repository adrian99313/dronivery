import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:dronivery/main.dart';

void main() {
  testWidgets('App renders main navigation shell', (WidgetTester tester) async {
    tester.view.physicalSize = const Size(1280, 800);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.resetPhysicalSize);

    await tester.pumpWidget(const MyApp());

    // Verify MainNavigationShell and key UI components are present
    expect(find.byType(MaterialApp), findsOneWidget);
    expect(find.byType(MainNavigationShell), findsOneWidget);
  });
}

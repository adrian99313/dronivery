import sys

code = '''import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dronivery - Autonomous Drone Restaurant Delivery',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        scaffoldBackgroundColor: const Color(0xFFF4F6F9),
        primaryColor: DroniveryColors.emeraldTeal,
        colorScheme: ColorScheme.fromSeed(
          seedColor: DroniveryColors.emeraldTeal,
          primary: DroniveryColors.emeraldTeal,
          secondary: DroniveryColors.electricOrange,
          tertiary: DroniveryColors.warmSunset,
          surface: Colors.white,
        ),
        fontFamily: 'Roboto',
        useMaterial3: true,
      ),
      home: const MainNavigationShell(),
    );
  }
}

/// Palette constants used across Dronivery.
class DroniveryColors {
  static const emeraldTeal = Color(0xFF00C853);
  static const deepEmerald = Color(0xFF0B8043);
  static const electricOrange = Color(0xFFFF6D00);
  static const warmSunset = Color(0xFFFFAB00);
  static const sidebarTint = Color(0xFFE8F5E9);
  static const darkSlate = Color(0xFF0F172A);
  static const surfaceSlate = Color(0xFF1E293B);
  static const bgLight = Color(0xFFF4F6F9);
  static const borderLight = Color(0xFFE2E8F0);
  static const textSubtle = Color(0xFF64748B);
}

// ==========================================
// DATA MODELS
// ==========================================

class MenuItem {
  const MenuItem({
    required this.id,
    required this.title,
    required this.description,
    required this.price,
    required this.imageUrl,
    required this.icon,
    this.category = 'Popular',
  });

  final String id;
  final String title;
  final String description;
  final double price;
  final String imageUrl;
  final IconData icon;
  final String category;
}

class Restaurant {
  const Restaurant({
    required this.id,
    required this.name,
    required this.cuisine,
    required this.tagline,
    required this.rating,
    required this.reviewCount,
    required this.flightTime,
    required this.distance,
    required this.imageUrl,
    required this.priceTier,
    required this.menuItems,
    required this.headerColor,
  });

  final String id;
  final String name;
  final String cuisine;
  final String tagline;
  final double rating;
  final int reviewCount;
  final String flightTime;
  final String distance;
  final String imageUrl;
  final String priceTier;
  final List<MenuItem> menuItems;
  final Color headerColor;
}

class ActiveOrder {
  ActiveOrder({
    required this.orderId,
    required this.restaurantName,
    required this.itemsCount,
    required this.totalAmount,
    required this.estimatedMinutes,
  });

  final String orderId;
  final String restaurantName;
  final int itemsCount;
  final double totalAmount;
  int estimatedMinutes;
  double progress = 0.35;
}

// Sample Restaurants Catalog
final sampleRestaurants = [
  Restaurant(
    id: 'rest_sushi',
    name: 'Sakura Drone Sushi Bar',
    cuisine: 'Asian',
    tagline: 'Hand-rolled dragon rolls & wild fresh sashimi',
    rating: 4.9,
    reviewCount: 320,
    flightTime: '12 min',
    distance: '1.8 mi',
    priceTier: '$$$',
    imageUrl: 'https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=600&auto=format&fit=crop',
    headerColor: const Color(0xFF2E1065),
    menuItems: const [
      MenuItem(
        id: 'm1',
        title: 'Dragon Roll & Nigiri Set',
        description: 'Fresh salmon, avocado, spicy mayo, eel sauce drizzle',
        price: 18.99,
        imageUrl: 'https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=500&auto=format&fit=crop',
        icon: Icons.set_meal_rounded,
        category: 'Popular',
      ),
      MenuItem(
        id: 'm2',
        title: 'Wild Salmon Sashimi (6pcs)',
        description: 'Premium sushi grade wild king salmon slices',
        price: 22.50,
        imageUrl: 'https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=500&auto=format&fit=crop',
        icon: Icons.set_meal_rounded,
        category: 'Mains',
      ),
      MenuItem(
        id: 'm3',
        title: 'Spicy Tuna Crunch Roll',
        description: 'Yellowfin tuna, cucumber, tempura flakes, sriracha',
        price: 13.99,
        imageUrl: 'https://images.unsplash.com/photo-1611143669185-af224c5e3252?w=500&auto=format&fit=crop',
        icon: Icons.set_meal_rounded,
        category: 'Popular',
      ),
      MenuItem(
        id: 'm4',
        title: 'Organic Steamed Edamame',
        description: 'Tossed with Maldon sea salt flakes',
        price: 5.50,
        imageUrl: 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=500&auto=format&fit=crop',
        icon: Icons.grass_rounded,
        category: 'Sides',
      ),
    ],
  ),
  Restaurant(
    id: 'rest_ramen',
    name: 'Tokyo Ramen Air Corridor',
    cuisine: 'Asian',
    tagline: '24-hour tonkotsu broth & handmade gyoza',
    rating: 4.8,
    reviewCount: 210,
    flightTime: '14 min',
    distance: '2.5 mi',
    priceTier: '$$',
    imageUrl: 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600&auto=format&fit=crop',
    headerColor: const Color(0xFF7F1D1D),
    menuItems: const [
      MenuItem(
        id: 'm5',
        title: 'Spicy Tonkotsu Chashu Ramen',
        description: 'Rich pork bone broth, soft-boiled egg, tender chashu belly',
        price: 16.50,
        imageUrl: 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=500&auto=format&fit=crop',
        icon: Icons.ramen_dining_rounded,
        category: 'Popular',
      ),
      MenuItem(
        id: 'm6',
        title: 'Pan-Seared Pork Gyoza (6pcs)',
        description: 'Crispy bottoms with ginger soy dipping sauce',
        price: 8.99,
        imageUrl: 'https://images.unsplash.com/photo-1496116218417-1a781b1c416c?w=500&auto=format&fit=crop',
        icon: Icons.lunch_dining_rounded,
        category: 'Sides',
      ),
    ],
  ),
  Restaurant(
    id: 'rest_taco',
    name: 'Taquería SkyTaco Express',
    cuisine: 'Mexican',
    tagline: 'Slow-cooked beef birria & fresh salsa bar',
    rating: 4.8,
    reviewCount: 450,
    flightTime: '15 min',
    distance: '1.4 mi',
    priceTier: '$$',
    imageUrl: 'https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=600&auto=format&fit=crop',
    headerColor: const Color(0xFF065F46),
    menuItems: const [
      MenuItem(
        id: 'm7',
        title: 'Birria Quesatacos Trio with Consomé',
        description: 'Melted cheese, braised beef birria, warm dipping broth',
        price: 16.99,
        imageUrl: 'https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=500&auto=format&fit=crop',
        icon: Icons.lunch_dining_rounded,
        category: 'Popular',
      ),
      MenuItem(
        id: 'm8',
        title: 'Carne Asada Street Tacos (3pcs)',
        description: 'Grilled steak, chopped cilantro, diced white onions, salsa verde',
        price: 14.50,
        imageUrl: 'https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?w=500&auto=format&fit=crop',
        icon: Icons.lunch_dining_rounded,
        category: 'Mains',
      ),
      MenuItem(
        id: 'm9',
        title: 'House Guacamole & Tortilla Chips',
        description: 'Hass avocados, lime, jalapeño, sea salt',
        price: 6.99,
        imageUrl: 'https://images.unsplash.com/photo-1541544741938-0af808871cc0?w=500&auto=format&fit=crop',
        icon: Icons.tapas_rounded,
        category: 'Sides',
      ),
    ],
  ),
  Restaurant(
    id: 'rest_indian',
    name: 'Taj Mahal Sky Kitchen',
    cuisine: 'Indian',
    tagline: 'Royal butter chicken & clay oven garlic naan',
    rating: 4.9,
    reviewCount: 510,
    flightTime: '14 min',
    distance: '2.2 mi',
    priceTier: '$$',
    imageUrl: 'https://images.unsplash.com/photo-1588166524941-3bf61a9c41db?w=600&auto=format&fit=crop',
    headerColor: const Color(0xFF78350F),
    menuItems: const [
      MenuItem(
        id: 'm10',
        title: 'Royal Butter Chicken & Basmati Rice',
        description: 'Tender chicken pieces in rich creamy tomato butter sauce',
        price: 16.99,
        imageUrl: 'https://images.unsplash.com/photo-1588166524941-3bf61a9c41db?w=500&auto=format&fit=crop',
        icon: Icons.soup_kitchen_rounded,
        category: 'Popular',
      ),
      MenuItem(
        id: 'm11',
        title: 'Garlic Butter Tandoori Naan',
        description: 'Freshly baked in clay oven with cilantro',
        price: 3.99,
        imageUrl: 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=500&auto=format&fit=crop',
        icon: Icons.bakery_dining_rounded,
        category: 'Sides',
      ),
      MenuItem(
        id: 'm12',
        title: 'Crispy Vegetable Samosas (2pcs)',
        description: 'Stuffed with spiced potatoes & green peas',
        price: 6.50,
        imageUrl: 'https://images.unsplash.com/photo-1601050690597-df0568f70950?w=500&auto=format&fit=crop',
        icon: Icons.local_dining_rounded,
        category: 'Sides',
      ),
    ],
  ),
  Restaurant(
    id: 'rest_middle_eastern',
    name: "Sultan's Charcoal Grill",
    cuisine: 'Middle Eastern',
    tagline: 'Flame-charred kabobs, shawarma & creamy hummus',
    rating: 4.8,
    reviewCount: 290,
    flightTime: '16 min',
    distance: '2.6 mi',
    priceTier: '$$',
    imageUrl: 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=600&auto=format&fit=crop',
    headerColor: const Color(0xFF581C87),
    menuItems: const [
      MenuItem(
        id: 'm13',
        title: 'Charcoal Chicken Kabob Platter',
        description: 'Marinated saffron chicken skewers, saffron rice, garlic toum',
        price: 17.25,
        imageUrl: 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=500&auto=format&fit=crop',
        icon: Icons.kebab_dining_rounded,
        category: 'Popular',
      ),
      MenuItem(
        id: 'm14',
        title: 'Lamb Shawarma Wrap',
        description: 'Spiced slow-roasted lamb, tahini sauce, pickled turnips in warm pita',
        price: 15.50,
        imageUrl: 'https://images.unsplash.com/photo-1561651823-34feb02250e4?w=500&auto=format&fit=crop',
        icon: Icons.kebab_dining_rounded,
        category: 'Mains',
      ),
      MenuItem(
        id: 'm15',
        title: 'Artisan Creamy Hummus & Warm Pita',
        description: 'Drizzled with Extra Virgin Olive Oil and paprika',
        price: 7.00,
        imageUrl: 'https://images.unsplash.com/photo-1541518763669-27fef04b14ea?w=500&auto=format&fit=crop',
        icon: Icons.rice_bowl_rounded,
        category: 'Sides',
      ),
    ],
  ),
  Restaurant(
    id: 'rest_italian',
    name: 'Bella Italia Wood-Fired Pizzeria',
    cuisine: 'Italian',
    tagline: 'Neapolitan pizzas & hand-rolled fettuccine',
    rating: 4.9,
    reviewCount: 620,
    flightTime: '13 min',
    distance: '1.2 mi',
    priceTier: '$$',
    imageUrl: 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&auto=format&fit=crop',
    headerColor: const Color(0xFF1E3A8A),
    menuItems: const [
      MenuItem(
        id: 'm16',
        title: 'Truffle Mushroom Wood-Fired Pizza',
        description: 'Wild mushrooms, mozzarella, black truffle oil, fresh basil',
        price: 19.50,
        imageUrl: 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500&auto=format&fit=crop',
        icon: Icons.local_pizza_rounded,
        category: 'Popular',
      ),
      MenuItem(
        id: 'm17',
        title: 'Fettuccine Alfredo & Crisp Pancetta',
        description: 'Handmade pasta, Parmigiano-Reggiano cream sauce',
        price: 16.50,
        imageUrl: 'https://images.unsplash.com/photo-1621996346565-e3d5d6281316?w=500&auto=format&fit=crop',
        icon: Icons.dinner_dining_rounded,
        category: 'Mains',
      ),
      MenuItem(
        id: 'm18',
        title: 'Sicilian Ricotta Cannoli (2pcs)',
        description: 'Crispy shells filled with sweet ricotta and pistachio bits',
        price: 6.50,
        imageUrl: 'https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=500&auto=format&fit=crop',
        icon: Icons.icecream_rounded,
        category: 'Desserts',
      ),
    ],
  ),
  Restaurant(
    id: 'rest_burger',
    name: 'Smash & Fly Burger Co.',
    cuisine: 'Burgers',
    tagline: 'Crispy smash burgers, truffle fries & thick shakes',
    rating: 4.8,
    reviewCount: 410,
    flightTime: '11 min',
    distance: '0.9 mi',
    priceTier: '$',
    imageUrl: 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&auto=format&fit=crop',
    headerColor: const Color(0xFF831843),
    menuItems: const [
      MenuItem(
        id: 'm19',
        title: 'Double Smash Cheeseburger',
        description: 'Angus beef patties, melted sharp cheddar, house sauce, brioche bun',
        price: 13.99,
        imageUrl: 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500&auto=format&fit=crop',
        icon: Icons.fastfood_rounded,
        category: 'Popular',
      ),
      MenuItem(
        id: 'm20',
        title: 'Truffle Parmesan Hand-Cut Fries',
        description: 'Tossed in truffle oil, herbs, and aged parmesan cheese',
        price: 5.50,
        imageUrl: 'https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=500&auto=format&fit=crop',
        icon: Icons.local_drink_rounded,
        category: 'Sides',
      ),
      MenuItem(
        id: 'm21',
        title: 'Hand-Spun Double Chocolate Milkshake',
        description: 'Real vanilla bean ice cream with Belgian fudge sauce',
        price: 4.99,
        imageUrl: 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=500&auto=format&fit=crop',
        icon: Icons.local_drink_rounded,
        category: 'Drinks',
      ),
    ],
  ),
];

// ==========================================
// UTILITY WIDGETS
// ==========================================

class SafeNetworkImage extends StatelessWidget {
  const SafeNetworkImage({
    super.key,
    required this.imageUrl,
    this.height,
    this.width = double.infinity,
    this.fit = BoxFit.cover,
    this.fallbackIcon = Icons.fastfood_rounded,
    this.fallbackTitle = 'Dronivery Restaurant',
    this.fallbackBgColor,
    this.borderRadius,
  });

  final String imageUrl;
  final double? height;
  final double width;
  final BoxFit fit;
  final IconData fallbackIcon;
  final String fallbackTitle;
  final Color? fallbackBgColor;
  final BorderRadius? borderRadius;

  @override
  Widget build(BuildContext context) {
    final bg = fallbackBgColor ?? DroniveryColors.surfaceSlate;

    Widget imageWidget = Image.network(
      imageUrl,
      height: height,
      width: width,
      fit: fit,
      loadingBuilder: (context, child, loadingProgress) {
        if (loadingProgress == null) return child;
        return Container(
          height: height,
          width: width,
          decoration: BoxDecoration(
            color: const Color(0xFFE2E8F0),
            borderRadius: borderRadius,
          ),
          child: const Center(
            child: SizedBox(
              width: 24,
              height: 24,
              child: CircularProgressIndicator(
                strokeWidth: 2.5,
                color: DroniveryColors.emeraldTeal,
              ),
            ),
          ),
        );
      },
      errorBuilder: (context, error, stackTrace) {
        return Container(
          height: height,
          width: width,
          decoration: BoxDecoration(
            color: bg,
            gradient: LinearGradient(
              colors: [bg, bg.withOpacity(0.85)],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
            borderRadius: borderRadius,
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(fallbackIcon, size: 36, color: DroniveryColors.emeraldTeal),
              const SizedBox(height: 6),
              Text(
                fallbackTitle,
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 12,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
        );
      },
    );

    if (borderRadius != null) {
      return ClipRRect(
        borderRadius: borderRadius!,
        child: imageWidget,
      );
    }
    return imageWidget;
  }
}

// ==========================================
// APPLICATION NAVIGATION SHELL & STATE
// ==========================================

class MainNavigationShell extends StatefulWidget {
  const MainNavigationShell({super.key});

  @override
  State<MainNavigationShell> createState() => _MainNavigationShellState();
}

class _MainNavigationShellState extends State<MainNavigationShell> {
  int _selectedIndex = 0;
  bool _isGoldMember = false;

  final Map<MenuItem, int> _cart = {};
  String _appliedPromoCode = '';
  double _appliedDiscount = 0.0;

  String _searchQuery = '';
  String _selectedCategory = 'All';
  String _selectedFilter = 'All';

  ActiveOrder? _activeOrder;

  void _onNavSelected(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  void _toggleGoldMembership() {
    setState(() {
      _isGoldMember = !_isGoldMember;
    });
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(
          _isGoldMember
              ? '⚡ Dronivery Gold Activated! Zero delivery fees unlocked.'
              : 'Membership updated.',
        ),
        backgroundColor: DroniveryColors.emeraldTeal,
        behavior: SnackBarBehavior.floating,
      ),
    );
  }

  void _addToCart(MenuItem item) {
    setState(() {
      _cart[item] = (_cart[item] ?? 0) + 1;
    });
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('Added ${item.title} to drone payload!'),
        duration: const Duration(seconds: 2),
        backgroundColor: DroniveryColors.darkSlate,
        behavior: SnackBarBehavior.floating,
      ),
    );
  }

  void _removeFromCart(MenuItem item) {
    setState(() {
      if (_cart.containsKey(item)) {
        if (_cart[item]! > 1) {
          _cart[item] = _cart[item]! - 1;
        } else {
          _cart.remove(item);
        }
      }
    });
  }

  void _applyPromoCode(String code) {
    final cleanCode = code.trim().toUpperCase();
    if (cleanCode == 'FIRSTFLY') {
      setState(() {
        _appliedPromoCode = 'FIRSTFLY';
        _appliedDiscount = 10.0;
      });
      _showToast('Promo "FIRSTFLY" applied! \$10 discount.');
    } else if (cleanCode == 'DRONEFREE') {
      setState(() {
        _appliedPromoCode = 'DRONEFREE';
        _appliedDiscount = 2.99;
      });
      _showToast('Promo "DRONEFREE" applied! Free delivery.');
    } else if (cleanCode == 'GOLDFLASH') {
      setState(() {
        _appliedPromoCode = 'GOLDFLASH';
        _appliedDiscount = _calculateSubtotal() * 0.30;
      });
      _showToast('Promo "GOLDFLASH" applied! 30% discount.');
    } else if (cleanCode == 'NIGHTOWL') {
      setState(() {
        _appliedPromoCode = 'NIGHTOWL';
        _appliedDiscount = _calculateSubtotal() * 0.15;
      });
      _showToast('Promo "NIGHTOWL" applied! 15% discount.');
    } else {
      _showToast('Invalid promo code.');
    }
  }

  void _showToast(String msg) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(msg),
        backgroundColor: DroniveryColors.emeraldTeal,
        behavior: SnackBarBehavior.floating,
      ),
    );
  }

  double _calculateSubtotal() {
    double total = 0.0;
    _cart.forEach((item, count) {
      total += item.price * count;
    });
    return total;
  }

  int get _totalCartCount => _cart.values.fold(0, (sum, item) => sum + item);

  void _openCartModal() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => CartDrawerModal(
        cart: _cart,
        onAdd: _addToCart,
        onRemove: _removeFromCart,
        isGoldMember: _isGoldMember,
        appliedPromoCode: _appliedPromoCode,
        appliedDiscount: _appliedDiscount,
        onApplyPromo: _applyPromoCode,
        onDispatchOrder: () {
          Navigator.of(context).pop();
          _dispatchDroneOrder();
        },
      ),
    );
  }

  void _dispatchDroneOrder() {
    if (_cart.isEmpty) return;

    final subtotal = _calculateSubtotal();
    final deliveryFee = _isGoldMember ? 0.0 : 2.99;
    final total = (subtotal - _appliedDiscount + deliveryFee).clamp(0.0, 9999.0);

    final newOrder = ActiveOrder(
      orderId: '#DR-${(1000 + _cart.length * 142) % 9000 + 1000}',
      restaurantName: _cart.keys.first.title,
      itemsCount: _totalCartCount,
      totalAmount: total,
      estimatedMinutes: 14,
    );

    setState(() {
      _activeOrder = newOrder;
      _cart.clear();
      _appliedPromoCode = '';
      _appliedDiscount = 0.0;
    });

    _showDroneDispatchConfirmationModal(newOrder);
  }

  void _showDroneDispatchConfirmationModal(ActiveOrder order) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
        backgroundColor: Colors.white,
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              padding: const EdgeInsets.all(20),
              decoration: const BoxDecoration(
                color: DroniveryColors.sidebarTint,
                shape: BoxShape.circle,
              ),
              child: const Icon(Icons.flight_takeoff_rounded, color: DroniveryColors.emeraldTeal, size: 54),
            ),
            const SizedBox(height: 16),
            Text(
              'Drone Air Dispatch Confirmed!',
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900, color: DroniveryColors.darkSlate),
            ),
            const SizedBox(height: 8),
            Text(
              'Order ${order.orderId} is loaded in thermal payload bay. Flight radar active at 200ft altitude.',
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 13, color: DroniveryColors.textSubtle),
            ),
            const SizedBox(height: 20),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              decoration: BoxDecoration(
                color: DroniveryColors.darkSlate,
                borderRadius: BorderRadius.circular(14),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  const Text('Estimated Delivery:', style: TextStyle(color: Colors.white, fontSize: 13)),
                  Text('⚡ ${order.estimatedMinutes} Minutes', style: const TextStyle(color: DroniveryColors.emeraldTeal, fontWeight: FontWeight.w900, fontSize: 14)),
                ],
              ),
            ),
            const SizedBox(height: 24),
            SizedBox(
              width: double.infinity,
              height: 48,
              child: ElevatedButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: DroniveryColors.emeraldTeal,
                  foregroundColor: Colors.white,
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
                ),
                child: const Text('Track Live Flight Radar', style: TextStyle(fontWeight: FontWeight.w900)),
              ),
            ),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final screenWidth = MediaQuery.of(context).size.width;
    final isDesktop = screenWidth >= 900;

    final pages = [
      OrderDeliveryScreen(
        searchQuery: _searchQuery,
        onSearchChanged: (q) => setState(() => _searchQuery = q),
        selectedCategory: _selectedCategory,
        onCategorySelected: (cat) => setState(() => _selectedCategory = cat),
        selectedFilter: _selectedFilter,
        onFilterSelected: (f) => setState(() => _selectedFilter = f),
        cart: _cart,
        onAddToCart: _addToCart,
        onRemoveFromCart: _removeFromCart,
        isGoldMember: _isGoldMember,
        onUpgradePressed: () => _onNavSelected(3),
        onOpenCart: _openCartModal,
        activeOrder: _activeOrder,
      ),
      const AboutUsScreen(),
      PromoScreen(
        isGoldMember: _isGoldMember,
        onUpgradePressed: () => _onNavSelected(3),
        onApplyPromoToCart: (code) {
          _applyPromoCode(code);
          _openCartModal();
        },
      ),
      GoldMemberScreen(
        isGoldMember: _isGoldMember,
        onToggleGold: _toggleGoldMembership,
      ),
    ];

    if (isDesktop) {
      return Scaffold(
        body: Row(
          children: [
            SidebarNav(
              selectedIndex: _selectedIndex,
              onNavSelected: _onNavSelected,
              isGoldMember: _isGoldMember,
              cartCount: _totalCartCount,
            ),
            Expanded(
              child: Column(
                children: [
                  _TopHeader(
                    cartCount: _totalCartCount,
                    isGoldMember: _isGoldMember,
                    onGoldTap: () => _onNavSelected(3),
                    onOpenCart: _openCartModal,
                  ),
                  Expanded(
                    child: Container(
                      width: double.infinity,
                      color: DroniveryColors.bgLight,
                      child: IndexedStack(
                        index: _selectedIndex,
                        children: pages,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      );
    }

    final navTitles = ['Order Delivery', 'About Us', 'Promo', 'Gold Member'];

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white,
        elevation: 0.5,
        title: Row(
          children: [
            const Icon(Icons.flight_takeoff, color: DroniveryColors.emeraldTeal),
            const SizedBox(width: 8),
            Text(
              navTitles[_selectedIndex],
              style: const TextStyle(
                color: DroniveryColors.darkSlate,
                fontWeight: FontWeight.bold,
                fontSize: 18,
              ),
            ),
          ],
        ),
        actions: [
          if (_isGoldMember)
            Padding(
              padding: const EdgeInsets.only(right: 8),
              child: Chip(
                avatar: const Icon(Icons.workspace_premium, color: Colors.black, size: 16),
                label: const Text('GOLD', style: TextStyle(fontWeight: FontWeight.w900, fontSize: 11)),
                backgroundColor: DroniveryColors.warmSunset,
                side: BorderSide.none,
              ),
            ),
          Stack(
            alignment: Alignment.center,
            children: [
              IconButton(
                icon: const Icon(Icons.shopping_bag_outlined, color: DroniveryColors.darkSlate),
                onPressed: _openCartModal,
              ),
              if (_totalCartCount > 0)
                Positioned(
                  right: 8,
                  top: 8,
                  child: Container(
                    padding: const EdgeInsets.all(4),
                    decoration: const BoxDecoration(
                      color: DroniveryColors.electricOrange,
                      shape: BoxShape.circle,
                    ),
                    child: Text(
                      '$_totalCartCount',
                      style: const TextStyle(color: Colors.white, fontSize: 10, fontWeight: FontWeight.bold),
                    ),
                  ),
                ),
            ],
          ),
          const SizedBox(width: 8),
        ],
      ),
      drawer: Drawer(
        child: SidebarNav(
          selectedIndex: _selectedIndex,
          onNavSelected: (idx) {
            _onNavSelected(idx);
            Navigator.of(context).pop();
          },
          isGoldMember: _isGoldMember,
          cartCount: _totalCartCount,
        ),
      ),
      body: Container(
        width: double.infinity,
        color: DroniveryColors.bgLight,
        child: IndexedStack(
          index: _selectedIndex,
          children: pages,
        ),
      ),
    );
  }
}

/// Top Header Bar for Desktop View
class _TopHeader extends StatelessWidget {
  const _TopHeader({
    required this.cartCount,
    required this.isGoldMember,
    required this.onGoldTap,
    required this.onOpenCart,
  });

  final int cartCount;
  final bool isGoldMember;
  final VoidCallback onGoldTap;
  final VoidCallback onOpenCart;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 72,
      padding: const EdgeInsets.symmetric(horizontal: 28),
      decoration: const BoxDecoration(
        color: Colors.white,
        border: Border(bottom: BorderSide(color: DroniveryColors.borderLight, width: 1)),
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: DroniveryColors.sidebarTint,
              borderRadius: BorderRadius.circular(10),
            ),
            child: const Icon(Icons.location_on, color: DroniveryColors.emeraldTeal, size: 20),
          ),
          const SizedBox(width: 12),
          Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: const [
              Text(
                'DRONE LAUNCH PAD LOCATION',
                style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: DroniveryColors.textSubtle, letterSpacing: 0.5),
              ),
              Text(
                '742 Evergreen Terrace (Zone A - Flight Ready)',
                style: TextStyle(fontSize: 13, fontWeight: FontWeight.w900, color: DroniveryColors.darkSlate),
              ),
            ],
          ),
          const Spacer(),
          GestureDetector(
            onTap: onGoldTap,
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 9),
              decoration: BoxDecoration(
                gradient: isGoldMember
                    ? const LinearGradient(colors: [DroniveryColors.warmSunset, Color(0xFFFF8F00)])
                    : null,
                color: isGoldMember ? null : DroniveryColors.sidebarTint,
                borderRadius: BorderRadius.circular(24),
                border: Border.all(
                  color: isGoldMember ? DroniveryColors.warmSunset : DroniveryColors.emeraldTeal.withOpacity(0.3),
                ),
              ),
              child: Row(
                children: [
                  Icon(
                    Icons.workspace_premium_rounded,
                    size: 18,
                    color: isGoldMember ? Colors.black : DroniveryColors.deepEmerald,
                  ),
                  const SizedBox(width: 6),
                  Text(
                    isGoldMember ? 'Gold Member Active' : 'Upgrade to Gold',
                    style: TextStyle(
                      fontSize: 13,
                      fontWeight: FontWeight.w900,
                      color: isGoldMember ? Colors.black : DroniveryColors.deepEmerald,
                    ),
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(width: 16),
          GestureDetector(
            onTap: onOpenCart,
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 9),
              decoration: BoxDecoration(
                color: DroniveryColors.darkSlate,
                borderRadius: BorderRadius.circular(24),
              ),
              child: Row(
                children: [
                  const Icon(Icons.shopping_bag_outlined, color: DroniveryColors.emeraldTeal, size: 18),
                  const SizedBox(width: 8),
                  Text(
                    '$cartCount Payload Items',
                    style: const TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                      fontSize: 13,
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

/// Sidebar Navigation
class SidebarNav extends StatelessWidget {
  const SidebarNav({
    super.key,
    required this.selectedIndex,
    required this.onNavSelected,
    required this.isGoldMember,
    required this.cartCount,
  });

  final int selectedIndex;
  final ValueChanged<int> onNavSelected;
  final bool isGoldMember;
  final int cartCount;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 270,
      color: Colors.white,
      padding: const EdgeInsets.all(22),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  gradient: const LinearGradient(
                    colors: [DroniveryColors.emeraldTeal, DroniveryColors.deepEmerald],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  borderRadius: BorderRadius.circular(14),
                  boxShadow: [
                    BoxShadow(
                      color: DroniveryColors.emeraldTeal.withOpacity(0.35),
                      blurRadius: 12,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
                child: const Icon(
                  Icons.flight_takeoff_rounded,
                  color: Colors.white,
                  size: 26,
                ),
              ),
              const SizedBox(width: 14),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: const [
                  Text(
                    'dronivery',
                    style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.w900,
                      color: DroniveryColors.darkSlate,
                      letterSpacing: -0.5,
                    ),
                  ),
                  Text(
                    'AIR LOGISTICS EXPRESS',
                    style: TextStyle(
                      fontSize: 9,
                      color: DroniveryColors.emeraldTeal,
                      fontWeight: FontWeight.w900,
                      letterSpacing: 0.8,
                    ),
                  ),
                ],
              ),
            ],
          ),
          const SizedBox(height: 36),

          _NavTile(
            icon: Icons.explore_rounded,
            label: 'Order Delivery',
            isSelected: selectedIndex == 0,
            onTap: () => onNavSelected(0),
          ),
          _NavTile(
            icon: Icons.info_outline_rounded,
            label: 'About Us',
            isSelected: selectedIndex == 1,
            onTap: () => onNavSelected(1),
          ),
          _NavTile(
            icon: Icons.local_offer_outlined,
            label: 'Promo',
            isSelected: selectedIndex == 2,
            onTap: () => onNavSelected(2),
          ),
          _NavTile(
            icon: Icons.workspace_premium_outlined,
            label: 'Gold Member',
            isSelected: selectedIndex == 3,
            badge: isGoldMember ? 'ACTIVE' : 'PREMIUM',
            onTap: () => onNavSelected(3),
          ),

          const Spacer(),

          GestureDetector(
            onTap: () => onNavSelected(3),
            child: Container(
              padding: const EdgeInsets.all(18),
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [DroniveryColors.darkSlate, DroniveryColors.surfaceSlate],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                borderRadius: BorderRadius.circular(18),
                border: Border.all(
                  color: isGoldMember ? DroniveryColors.warmSunset : Colors.transparent,
                  width: 1.5,
                ),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: const [
                      Icon(Icons.workspace_premium_rounded, color: DroniveryColors.warmSunset, size: 22),
                      SizedBox(width: 8),
                      Text(
                        'Members Get:',
                        style: TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.w900,
                          fontSize: 14,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 14),
                  const _MemberPerkRow(icon: Icons.radar, text: 'Priority Drone Routing'),
                  const SizedBox(height: 8),
                  const _MemberPerkRow(icon: Icons.money_off_rounded, text: 'Zero Delivery Fees'),
                  const SizedBox(height: 8),
                  const _MemberPerkRow(icon: Icons.map_outlined, text: 'Extended 20mi Range'),
                  const SizedBox(height: 16),
                  Container(
                    width: double.infinity,
                    padding: const EdgeInsets.symmetric(vertical: 10),
                    decoration: BoxDecoration(
                      gradient: isGoldMember
                          ? const LinearGradient(colors: [DroniveryColors.warmSunset, Color(0xFFFF8F00)])
                          : const LinearGradient(colors: [DroniveryColors.emeraldTeal, DroniveryColors.deepEmerald]),
                      borderRadius: BorderRadius.circular(24),
                    ),
                    child: Text(
                      isGoldMember ? 'View Gold Perks' : 'Join Gold \$9.99/mo',
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        color: isGoldMember ? Colors.black : Colors.white,
                        fontWeight: FontWeight.w900,
                        fontSize: 12,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class _NavTile extends StatelessWidget {
  const _NavTile({
    required this.icon,
    required this.label,
    required this.isSelected,
    required this.onTap,
    this.badge,
  });

  final IconData icon;
  final String label;
  final bool isSelected;
  final VoidCallback onTap;
  final String? badge;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 10),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(14),
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
          decoration: BoxDecoration(
            color: isSelected ? DroniveryColors.sidebarTint : Colors.transparent,
            borderRadius: BorderRadius.circular(14),
            border: Border.all(
              color: isSelected ? DroniveryColors.emeraldTeal : Colors.transparent,
              width: 1.5,
            ),
          ),
          child: Row(
            children: [
              Icon(
                icon,
                color: isSelected ? DroniveryColors.emeraldTeal : DroniveryColors.textSubtle,
                size: 22,
              ),
              const SizedBox(width: 14),
              Text(
                label,
                style: TextStyle(
                  color: isSelected ? DroniveryColors.deepEmerald : DroniveryColors.darkSlate,
                  fontWeight: isSelected ? FontWeight.w900 : FontWeight.w500,
                  fontSize: 14,
                ),
              ),
              if (badge != null) ...[
                const Spacer(),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                  decoration: BoxDecoration(
                    color: badge == 'ACTIVE' ? DroniveryColors.warmSunset : DroniveryColors.electricOrange,
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Text(
                    badge!,
                    style: TextStyle(
                      color: badge == 'ACTIVE' ? Colors.black : Colors.white,
                      fontSize: 9,
                      fontWeight: FontWeight.w900,
                    ),
                  ),
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }
}

class _MemberPerkRow extends StatelessWidget {
  const _MemberPerkRow({required this.icon, required this.text});

  final IconData icon;
  final String text;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Icon(icon, color: DroniveryColors.emeraldTeal, size: 15),
        const SizedBox(width: 10),
        Expanded(
          child: Text(
            text,
            style: const TextStyle(color: Color(0xFFCBD5E1), fontSize: 12),
          ),
        ),
      ],
    );
  }
}

// ==========================================
// SCREEN 1: ORDER DELIVERY (RESTAURANTS VIEW)
// ==========================================

class OrderDeliveryScreen extends StatelessWidget {
  const OrderDeliveryScreen({
    super.key,
    required this.searchQuery,
    required this.onSearchChanged,
    required this.selectedCategory,
    required this.onCategorySelected,
    required this.selectedFilter,
    required this.onFilterSelected,
    required this.cart,
    required this.onAddToCart,
    required this.onRemoveFromCart,
    required this.isGoldMember,
    required this.onUpgradePressed,
    required this.onOpenCart,
    this.activeOrder,
  });

  final String searchQuery;
  final ValueChanged<String> onSearchChanged;
  final String selectedCategory;
  final ValueChanged<String> onCategorySelected;
  final String selectedFilter;
  final ValueChanged<String> onFilterSelected;
  final Map<MenuItem, int> cart;
  final ValueChanged<MenuItem> onAddToCart;
  final ValueChanged<MenuItem> onRemoveFromCart;
  final bool isGoldMember;
  final VoidCallback onUpgradePressed;
  final VoidCallback onOpenCart;
  final ActiveOrder? activeOrder;

  @override
  Widget build(BuildContext context) {
    var filteredRestaurants = sampleRestaurants.where((rest) {
      final matchesSearch = rest.name.toLowerCase().contains(searchQuery.toLowerCase()) ||
          rest.cuisine.toLowerCase().contains(searchQuery.toLowerCase()) ||
          rest.menuItems.any((m) => m.title.toLowerCase().contains(searchQuery.toLowerCase()));
      final matchesCategory = selectedCategory == 'All' || rest.cuisine == selectedCategory;
      return matchesSearch && matchesCategory;
    }).toList();

    if (selectedFilter == 'Top Rated') {
      filteredRestaurants.sort((a, b) => b.rating.compareTo(a.rating));
    } else if (selectedFilter == 'Fastest Flight') {
      filteredRestaurants.sort((a, b) => a.flightTime.compareTo(b.flightTime));
    } else if (selectedFilter == 'Distance') {
      filteredRestaurants.sort((a, b) => a.distance.compareTo(b.distance));
    }

    return SingleChildScrollView(
      padding: const EdgeInsets.all(28),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _LiveDroneTrackerCard(isGoldMember: isGoldMember, activeOrder: activeOrder),
          const SizedBox(height: 24),

          // Search Input
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 20),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: DroniveryColors.borderLight),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withOpacity(0.04),
                  blurRadius: 10,
                  offset: const Offset(0, 4),
                ),
              ],
            ),
            child: TextField(
              onChanged: onSearchChanged,
              decoration: const InputDecoration(
                hintText: 'Search restaurants, sushi bars, taquerias, pizzerias, burgers...',
                hintStyle: TextStyle(color: DroniveryColors.textSubtle, fontSize: 14),
                icon: Icon(Icons.search, color: DroniveryColors.emeraldTeal, size: 24),
                border: InputBorder.none,
              ),
            ),
          ),
          const SizedBox(height: 24),

          _HeroBanner(onExploreTap: onUpgradePressed),
          const SizedBox(height: 36),

          const Text(
            "Restaurants by Cuisine",
            style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.w900,
              color: DroniveryColors.darkSlate,
            ),
          ),
          const SizedBox(height: 4),
          const Text(
            'Order from certified local kitchens, delivered by autonomous drone air corridors.',
            style: TextStyle(fontSize: 14, color: DroniveryColors.textSubtle),
          ),
          const SizedBox(height: 20),

          _CategorySelector(
            selectedCategory: selectedCategory,
            onCategorySelected: onCategorySelected,
          ),
          const SizedBox(height: 20),

          // Quick Filter Bar
          Row(
            children: [
              const Text('Sort by:', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13, color: DroniveryColors.textSubtle)),
              const SizedBox(width: 12),
              _FilterButton(title: 'All', isSelected: selectedFilter == 'All', onTap: () => onFilterSelected('All')),
              const SizedBox(width: 8),
              _FilterButton(title: 'Top Rated', isSelected: selectedFilter == 'Top Rated', onTap: () => onFilterSelected('Top Rated')),
              const SizedBox(width: 8),
              _FilterButton(title: 'Fastest Flight', isSelected: selectedFilter == 'Fastest Flight', onTap: () => onFilterSelected('Fastest Flight')),
              const SizedBox(width: 8),
              _FilterButton(title: 'Distance', isSelected: selectedFilter == 'Distance', onTap: () => onFilterSelected('Distance')),
            ],
          ),
          const SizedBox(height: 28),

          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                selectedCategory == 'All' ? 'Top Drone Delivered Kitchens' : '$selectedCategory Restaurants',
                style: const TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.w900,
                  color: DroniveryColors.darkSlate,
                ),
              ),
              Text(
                '${filteredRestaurants.length} restaurants open',
                style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: DroniveryColors.textSubtle),
              ),
            ],
          ),
          const SizedBox(height: 18),

          // Restaurants Grid
          LayoutBuilder(
            builder: (context, constraints) {
              int crossAxisCount = 3;
              if (constraints.maxWidth < 700) {
                crossAxisCount = 1;
              } else if (constraints.maxWidth < 1100) {
                crossAxisCount = 2;
              }

              if (filteredRestaurants.isEmpty) {
                return Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(40),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Column(
                    children: const [
                      Icon(Icons.search_off_rounded, size: 48, color: DroniveryColors.textSubtle),
                      SizedBox(height: 12),
                      Text('No restaurants match your search.', style: TextStyle(fontWeight: FontWeight.bold)),
                    ],
                  ),
                );
              }

              return GridView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: filteredRestaurants.length,
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: crossAxisCount,
                  crossAxisSpacing: 22,
                  mainAxisSpacing: 22,
                  childAspectRatio: 0.82,
                ),
                itemBuilder: (context, index) {
                  final rest = filteredRestaurants[index];
                  return RestaurantCard(
                    restaurant: rest,
                    cart: cart,
                    onAddToCart: onAddToCart,
                    onRemoveFromCart: onRemoveFromCart,
                  );
                },
              );
            },
          ),
        ],
      ),
    );
  }
}

class _FilterButton extends StatelessWidget {
  const _FilterButton({
    required this.title,
    required this.isSelected,
    required this.onTap,
  });

  final String title;
  final bool isSelected;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(12),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
        decoration: BoxDecoration(
          color: isSelected ? DroniveryColors.darkSlate : Colors.white,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(
            color: isSelected ? DroniveryColors.darkSlate : DroniveryColors.borderLight,
          ),
        ),
        child: Text(
          title,
          style: TextStyle(
            fontSize: 12,
            fontWeight: isSelected ? FontWeight.bold : FontWeight.w500,
            color: isSelected ? Colors.white : DroniveryColors.darkSlate,
          ),
        ),
      ),
    );
  }
}

class RestaurantCard extends StatelessWidget {
  const RestaurantCard({
    super.key,
    required this.restaurant,
    required this.cart,
    required this.onAddToCart,
    required this.onRemoveFromCart,
  });

  final Restaurant restaurant;
  final Map<MenuItem, int> cart;
  final ValueChanged<MenuItem> onAddToCart;
  final ValueChanged<MenuItem> onRemoveFromCart;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        showDialog(
          context: context,
          builder: (context) => RestaurantDetailDialog(
            restaurant: restaurant,
            cart: cart,
            onAddToCart: onAddToCart,
            onRemoveFromCart: onRemoveFromCart,
          ),
        );
      },
      child: Container(
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: DroniveryColors.borderLight),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.04),
              blurRadius: 12,
              offset: const Offset(0, 4),
            ),
          ],
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Expanded(
              flex: 5,
              child: Stack(
                children: [
                  SafeNetworkImage(
                    imageUrl: restaurant.imageUrl,
                    height: double.infinity,
                    width: double.infinity,
                    borderRadius: const BorderRadius.only(
                      topLeft: Radius.circular(20),
                      topRight: Radius.circular(20),
                    ),
                    fallbackIcon: Icons.store_rounded,
                    fallbackTitle: restaurant.name,
                    fallbackBgColor: restaurant.headerColor,
                  ),
                  Positioned(
                    top: 12,
                    left: 12,
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                      decoration: BoxDecoration(
                        color: DroniveryColors.darkSlate.withOpacity(0.85),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Text(
                        restaurant.cuisine.toUpperCase(),
                        style: const TextStyle(color: Colors.white, fontSize: 10, fontWeight: FontWeight.w900),
                      ),
                    ),
                  ),
                  Positioned(
                    top: 12,
                    right: 12,
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Row(
                        children: [
                          const Icon(Icons.flight_takeoff_rounded, color: DroniveryColors.emeraldTeal, size: 14),
                          const SizedBox(width: 4),
                          Text(
                            restaurant.flightTime,
                            style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w900, color: DroniveryColors.darkSlate),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
            Expanded(
              flex: 4,
              child: Padding(
                padding: const EdgeInsets.all(14),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Expanded(
                              child: Text(
                                restaurant.name,
                                maxLines: 1,
                                overflow: TextOverflow.ellipsis,
                                style: const TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.w900,
                                  color: DroniveryColors.darkSlate,
                                ),
                              ),
                            ),
                            Row(
                              children: [
                                const Icon(Icons.star_rounded, color: DroniveryColors.warmSunset, size: 16),
                                const SizedBox(width: 2),
                                Text(
                                  '${restaurant.rating}',
                                  style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w900),
                                ),
                                Text(
                                  ' (${restaurant.reviewCount})',
                                  style: const TextStyle(fontSize: 10, color: DroniveryColors.textSubtle),
                                ),
                              ],
                            ),
                          ],
                        ),
                        const SizedBox(height: 4),
                        Text(
                          restaurant.tagline,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: const TextStyle(fontSize: 12, color: DroniveryColors.textSubtle),
                        ),
                      ],
                    ),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Row(
                          children: [
                            Text(
                              restaurant.priceTier,
                              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 12, color: DroniveryColors.darkSlate),
                            ),
                            const SizedBox(width: 6),
                            const Icon(Icons.location_on_outlined, size: 12, color: DroniveryColors.textSubtle),
                            Text(
                              restaurant.distance,
                              style: const TextStyle(fontSize: 11, color: DroniveryColors.textSubtle),
                            ),
                          ],
                        ),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
                          decoration: BoxDecoration(
                            color: DroniveryColors.emeraldTeal,
                            borderRadius: BorderRadius.circular(20),
                          ),
                          child: const Text(
                            'View Menu',
                            style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.w900),
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

/// Restaurant Detail & Menu View Dialog
class RestaurantDetailDialog extends StatefulWidget {
  const RestaurantDetailDialog({
    super.key,
    required this.restaurant,
    required this.cart,
    required this.onAddToCart,
    required this.onRemoveFromCart,
  });

  final Restaurant restaurant;
  final Map<MenuItem, int> cart;
  final ValueChanged<MenuItem> onAddToCart;
  final ValueChanged<MenuItem> onRemoveFromCart;

  @override
  State<RestaurantDetailDialog> createState() => _RestaurantDetailDialogState();
}

class _RestaurantDetailDialogState extends State<RestaurantDetailDialog> {
  String _selectedTab = 'All';

  @override
  Widget build(BuildContext context) {
    final categories = ['All', ...widget.restaurant.menuItems.map((e) => e.category).toSet()];
    final displayItems = _selectedTab == 'All'
        ? widget.restaurant.menuItems
        : widget.restaurant.menuItems.where((e) => e.category == _selectedTab).toList();

    return Dialog(
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
      clipBehavior: Clip.antiAlias,
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 800, maxHeight: 720),
        child: Material(
          color: Colors.white,
          child: Column(
            children: [
              SizedBox(
                height: 180,
                child: Stack(
                  children: [
                    SafeNetworkImage(
                      imageUrl: widget.restaurant.imageUrl,
                      height: double.infinity,
                      width: double.infinity,
                      fallbackIcon: Icons.store_rounded,
                      fallbackTitle: widget.restaurant.name,
                      fallbackBgColor: widget.restaurant.headerColor,
                    ),
                    Container(
                      color: Colors.black.withOpacity(0.4),
                    ),
                    Positioned(
                      top: 16,
                      right: 16,
                      child: IconButton(
                        icon: const Icon(Icons.close, color: Colors.white, size: 28),
                        onPressed: () => Navigator.of(context).pop(),
                      ),
                    ),
                    Positioned(
                      bottom: 20,
                      left: 20,
                      right: 20,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                widget.restaurant.name,
                                style: const TextStyle(
                                  color: Colors.white,
                                  fontSize: 24,
                                  fontWeight: FontWeight.w900,
                                ),
                              ),
                              Text(
                                '${widget.restaurant.cuisine} • ${widget.restaurant.distance} • ⚡ ${widget.restaurant.flightTime}',
                                style: const TextStyle(color: Color(0xFFCBD5E1), fontSize: 13),
                              ),
                            ],
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),

              // Menu Subcategory Filter Tabs
              Container(
                height: 50,
                color: DroniveryColors.bgLight,
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                child: ListView.separated(
                  scrollDirection: Axis.horizontal,
                  itemCount: categories.length,
                  separatorBuilder: (_, __) => const SizedBox(width: 8),
                  itemBuilder: (context, idx) {
                    final tab = categories.elementAt(idx);
                    final isSel = _selectedTab == tab;

                    return ChoiceChip(
                      selected: isSel,
                      label: Text(tab),
                      selectedColor: DroniveryColors.emeraldTeal,
                      labelStyle: TextStyle(
                        color: isSel ? Colors.white : DroniveryColors.darkSlate,
                        fontWeight: isSel ? FontWeight.bold : FontWeight.w500,
                        fontSize: 12,
                      ),
                      side: BorderSide.none,
                      onSelected: (_) => setState(() => _selectedTab = tab),
                    );
                  },
                ),
              ),

              Expanded(
                child: ListView.separated(
                  padding: const EdgeInsets.all(24),
                  itemCount: displayItems.length,
                  separatorBuilder: (_, __) => const Divider(height: 32, color: DroniveryColors.borderLight),
                  itemBuilder: (context, index) {
                    final item = displayItems[index];
                    final itemCount = widget.cart[item] ?? 0;

                    return Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        ClipRRect(
                          borderRadius: BorderRadius.circular(12),
                          child: SafeNetworkImage(
                            imageUrl: item.imageUrl,
                            width: 90,
                            height: 90,
                            fallbackIcon: item.icon,
                            fallbackTitle: item.title,
                          ),
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                item.title,
                                style: const TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.w900,
                                  color: DroniveryColors.darkSlate,
                                ),
                              ),
                              const SizedBox(height: 4),
                              Text(
                                item.description,
                                style: const TextStyle(fontSize: 12, color: DroniveryColors.textSubtle),
                              ),
                              const SizedBox(height: 8),
                              Text(
                                '\$${item.price.toStringAsFixed(2)}',
                                style: const TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.w900,
                                  color: DroniveryColors.emeraldTeal,
                                ),
                              ),
                            ],
                          ),
                        ),
                        if (itemCount == 0)
                          ElevatedButton(
                            onPressed: () => widget.onAddToCart(item),
                            style: ElevatedButton.styleFrom(
                              backgroundColor: DroniveryColors.darkSlate,
                              foregroundColor: Colors.white,
                              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
                            ),
                            child: const Text('+ Add', style: TextStyle(fontWeight: FontWeight.w900, fontSize: 12)),
                          )
                        else
                          Container(
                            decoration: BoxDecoration(
                              color: DroniveryColors.sidebarTint,
                              borderRadius: BorderRadius.circular(20),
                            ),
                            child: Row(
                              children: [
                                IconButton(
                                  onPressed: () => widget.onRemoveFromCart(item),
                                  icon: const Icon(Icons.remove, size: 16, color: DroniveryColors.emeraldTeal),
                                  constraints: const BoxConstraints(minWidth: 32, minHeight: 32),
                                  padding: EdgeInsets.zero,
                                ),
                                Text(
                                  '$itemCount',
                                  style: const TextStyle(fontWeight: FontWeight.w900, fontSize: 13, color: DroniveryColors.darkSlate),
                                ),
                                IconButton(
                                  onPressed: () => widget.onAddToCart(item),
                                  icon: const Icon(Icons.add, size: 16, color: DroniveryColors.emeraldTeal),
                                  constraints: const BoxConstraints(minWidth: 32, minHeight: 32),
                                  padding: EdgeInsets.zero,
                                ),
                              ],
                            ),
                          ),
                      ],
                    );
                  },
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

// ==========================================
// CART & CHECKOUT DRAWER MODAL
// ==========================================

class CartDrawerModal extends StatefulWidget {
  const CartDrawerModal({
    super.key,
    required this.cart,
    required this.onAdd,
    required this.onRemove,
    required this.isGoldMember,
    required this.appliedPromoCode,
    required this.appliedDiscount,
    required this.onApplyPromo,
    required this.onDispatchOrder,
  });

  final Map<MenuItem, int> cart;
  final ValueChanged<MenuItem> onAdd;
  final ValueChanged<MenuItem> onRemove;
  final bool isGoldMember;
  final String appliedPromoCode;
  final double appliedDiscount;
  final ValueChanged<String> onApplyPromo;
  final VoidCallback onDispatchOrder;

  @override
  State<CartDrawerModal> createState() => _CartDrawerModalState();
}

class _CartDrawerModalState extends State<CartDrawerModal> {
  final TextEditingController _promoController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    double subtotal = 0.0;
    widget.cart.forEach((item, count) {
      subtotal += item.price * count;
    });

    final deliveryFee = widget.isGoldMember ? 0.0 : (subtotal > 0 ? 2.99 : 0.0);
    final discount = widget.appliedDiscount.clamp(0.0, subtotal);
    final total = (subtotal - discount + deliveryFee).clamp(0.0, 9999.0);

    return Container(
      height: MediaQuery.of(context).size.height * 0.85,
      decoration: const BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.only(
          topLeft: Radius.circular(28),
          topRight: Radius.circular(28),
        ),
      ),
      padding: const EdgeInsets.all(28),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              const Icon(Icons.shopping_bag_outlined, color: DroniveryColors.emeraldTeal, size: 24),
              const SizedBox(width: 10),
              const Text(
                'Drone Payload Cart',
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.w900, color: DroniveryColors.darkSlate),
              ),
              const Spacer(),
              IconButton(
                icon: const Icon(Icons.close, color: DroniveryColors.darkSlate),
                onPressed: () => Navigator.of(context).pop(),
              ),
            ],
          ),
          const Divider(height: 24, color: DroniveryColors.borderLight),

          if (widget.cart.isEmpty)
            Expanded(
              child: Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: const [
                    Icon(Icons.shopping_cart_outlined, size: 54, color: DroniveryColors.textSubtle),
                    SizedBox(height: 12),
                    Text(
                      'Your drone payload is currently empty.',
                      style: TextStyle(fontWeight: FontWeight.bold, color: DroniveryColors.darkSlate),
                    ),
                  ],
                ),
              ),
            )
          else ...[
            Expanded(
              child: ListView.separated(
                itemCount: widget.cart.keys.length,
                separatorBuilder: (_, __) => const SizedBox(height: 12),
                itemBuilder: (context, index) {
                  final item = widget.cart.keys.elementAt(index);
                  final count = widget.cart[item]!;

                  return Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: DroniveryColors.bgLight,
                      borderRadius: BorderRadius.circular(14),
                    ),
                    child: Row(
                      children: [
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(item.title, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14)),
                              Text('\$${item.price.toStringAsFixed(2)} each', style: const TextStyle(fontSize: 12, color: DroniveryColors.textSubtle)),
                            ],
                          ),
                        ),
                        Row(
                          children: [
                            IconButton(
                              onPressed: () => widget.onRemove(item),
                              icon: const Icon(Icons.remove_circle_outline, color: DroniveryColors.emeraldTeal, size: 20),
                            ),
                            Text('$count', style: const TextStyle(fontWeight: FontWeight.w900)),
                            IconButton(
                              onPressed: () => widget.onAdd(item),
                              icon: const Icon(Icons.add_circle_outline, color: DroniveryColors.emeraldTeal, size: 20),
                            ),
                          ],
                        ),
                        Text('\$${(item.price * count).toStringAsFixed(2)}', style: const TextStyle(fontWeight: FontWeight.w900)),
                      ],
                    ),
                  );
                },
              ),
            ),
            const SizedBox(height: 16),

            Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _promoController,
                    decoration: const InputDecoration(
                      hintText: 'Enter Promo Code (e.g. FIRSTFLY)',
                      hintStyle: TextStyle(fontSize: 12),
                      border: OutlineInputBorder(),
                      contentPadding: EdgeInsets.symmetric(horizontal: 12, vertical: 10),
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                ElevatedButton(
                  onPressed: () => widget.onApplyPromo(_promoController.text),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: DroniveryColors.darkSlate,
                    foregroundColor: Colors.white,
                  ),
                  child: const Text('Apply'),
                ),
              ],
            ),
            const SizedBox(height: 16),

            Column(
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Text('Subtotal:', style: TextStyle(color: DroniveryColors.textSubtle)),
                    Text('\$${subtotal.toStringAsFixed(2)}', style: const TextStyle(fontWeight: FontWeight.bold)),
                  ],
                ),
                if (widget.appliedDiscount > 0) ...[
                  const SizedBox(height: 4),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('Discount (${widget.appliedPromoCode}):', style: const TextStyle(color: DroniveryColors.emeraldTeal, fontWeight: FontWeight.bold)),
                      Text('-\$${discount.toStringAsFixed(2)}', style: const TextStyle(color: DroniveryColors.emeraldTeal, fontWeight: FontWeight.bold)),
                    ],
                  ),
                ],
                const SizedBox(height: 4),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text('Drone Air Fee:', style: const TextStyle(color: DroniveryColors.textSubtle)),
                    Text(
                      widget.isGoldMember ? 'FREE (Gold Member)' : '\$${deliveryFee.toStringAsFixed(2)}',
                      style: TextStyle(fontWeight: FontWeight.bold, color: widget.isGoldMember ? DroniveryColors.emeraldTeal : DroniveryColors.darkSlate),
                    ),
                  ],
                ),
                const Divider(height: 16),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Text('Total:', style: TextStyle(fontSize: 18, fontWeight: FontWeight.w900)),
                    Text('\$${total.toStringAsFixed(2)}', style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w900, color: DroniveryColors.emeraldTeal)),
                  ],
                ),
              ],
            ),
            const SizedBox(height: 20),

            SizedBox(
              width: double.infinity,
              height: 52,
              child: ElevatedButton.icon(
                onPressed: widget.onDispatchOrder,
                icon: const Icon(Icons.rocket_launch_rounded, size: 20),
                label: const Text('Dispatch Autonomous Drone Delivery'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: DroniveryColors.emeraldTeal,
                  foregroundColor: Colors.white,
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(28)),
                ),
              ),
            ),
          ],
        ],
      ),
    );
  }
}

class _LiveDroneTrackerCard extends StatelessWidget {
  const _LiveDroneTrackerCard({
    required this.isGoldMember,
    this.activeOrder,
  });

  final bool isGoldMember;
  final ActiveOrder? activeOrder;

  @override
  Widget build(BuildContext context) {
    final hasActive = activeOrder != null;
    final orderId = hasActive ? activeOrder!.orderId : '#DR-809';
    final eta = hasActive ? '${activeOrder!.estimatedMinutes} MINS' : '8 MINS';
    final progress = hasActive ? activeOrder!.progress : 0.70;

    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(22),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: DroniveryColors.emeraldTeal.withOpacity(0.5), width: 1.5),
        boxShadow: [
          BoxShadow(
            color: DroniveryColors.emeraldTeal.withOpacity(0.12),
            blurRadius: 18,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: DroniveryColors.sidebarTint,
                  shape: BoxShape.circle,
                ),
                child: const Icon(Icons.radar, color: DroniveryColors.emeraldTeal, size: 22),
              ),
              const SizedBox(width: 14),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Text(
                        'Live Flight Status: Drone $orderId',
                        style: const TextStyle(
                          fontWeight: FontWeight.w900,
                          fontSize: 16,
                          color: DroniveryColors.darkSlate,
                        ),
                      ),
                      const SizedBox(width: 10),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                        decoration: BoxDecoration(
                          color: DroniveryColors.emeraldTeal,
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: const Text(
                          'IN AIR',
                          style: TextStyle(color: Colors.white, fontSize: 10, fontWeight: FontWeight.w900),
                        ),
                      ),
                    ],
                  ),
                  Text(
                    isGoldMember ? '⚡ Priority Drone Routing Active (Zero Flight Delay)' : 'Standard Skyway Corridor',
                    style: const TextStyle(fontSize: 12, color: DroniveryColors.textSubtle),
                  ),
                ],
              ),
              const Spacer(),
              Column(
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Text(
                    '⚡ $eta',
                    style: const TextStyle(
                      color: DroniveryColors.emeraldTeal,
                      fontWeight: FontWeight.w900,
                      fontSize: 18,
                    ),
                  ),
                  const Text('200 ft Air Corridor', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: DroniveryColors.textSubtle)),
                ],
              ),
            ],
          ),
          const SizedBox(height: 18),

          ClipRRect(
            borderRadius: BorderRadius.circular(10),
            child: LinearProgressIndicator(
              value: progress,
              minHeight: 10,
              backgroundColor: const Color(0xFFE2E8F0),
              color: DroniveryColors.emeraldTeal,
            ),
          ),
          const SizedBox(height: 8),

          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: const [
              Text('Kitchen Loaded', style: TextStyle(fontSize: 11, color: DroniveryColors.textSubtle)),
              Text('Autonomous Flight', style: TextStyle(fontSize: 11, fontWeight: FontWeight.w900, color: DroniveryColors.emeraldTeal)),
              Text('Tether Drop Zone', style: TextStyle(fontSize: 11, color: DroniveryColors.textSubtle)),
            ],
          ),
        ],
      ),
    );
  }
}

class _HeroBanner extends StatelessWidget {
  const _HeroBanner({required this.onExploreTap});

  final VoidCallback onExploreTap;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      height: 230,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(24),
        gradient: const LinearGradient(
          colors: [Color(0xFF0F172A), Color(0xFF1E293B)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.18),
            blurRadius: 20,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: Stack(
        children: [
          Positioned(
            right: 0,
            top: 0,
            bottom: 0,
            width: 420,
            child: Opacity(
              opacity: 0.45,
              child: SafeNetworkImage(
                imageUrl: 'https://images.unsplash.com/photo-1527977966376-1c8408f9f108?w=800&auto=format&fit=crop',
                height: double.infinity,
                width: double.infinity,
                fit: BoxFit.cover,
                borderRadius: const BorderRadius.only(
                  topRight: Radius.circular(24),
                  bottomRight: Radius.circular(24),
                ),
                fallbackIcon: Icons.flight_takeoff,
                fallbackTitle: 'Autonomous Air Delivery',
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(32),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 5),
                  decoration: BoxDecoration(
                    color: DroniveryColors.emeraldTeal,
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: const Text(
                    'Sky-to-door in under 25 min',
                    style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.w900),
                  ),
                ),
                const SizedBox(height: 12),
                const Text(
                  'Crave it. Tap it.\nWe fly it.',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 32,
                    fontWeight: FontWeight.w900,
                    height: 1.1,
                  ),
                ),
                const SizedBox(height: 16),
                ElevatedButton.icon(
                  onPressed: onExploreTap,
                  icon: const Icon(Icons.workspace_premium_rounded, size: 18),
                  label: const Text('Get Priority Gold Drone Flight'),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: DroniveryColors.electricOrange,
                    foregroundColor: Colors.white,
                    padding: const EdgeInsets.symmetric(horizontal: 22, vertical: 14),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(30)),
                    elevation: 4,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _CategorySelector extends StatelessWidget {
  const _CategorySelector({
    required this.selectedCategory,
    required this.onCategorySelected,
  });

  final String selectedCategory;
  final ValueChanged<String> onCategorySelected;

  static const categories = [
    {'name': 'All', 'icon': Icons.restaurant_menu_rounded, 'color': DroniveryColors.emeraldTeal},
    {'name': 'Asian', 'icon': Icons.set_meal_rounded, 'color': Colors.redAccent},
    {'name': 'Mexican', 'icon': Icons.lunch_dining_rounded, 'color': DroniveryColors.emeraldTeal},
    {'name': 'Indian', 'icon': Icons.ramen_dining_rounded, 'color': DroniveryColors.warmSunset},
    {'name': 'Middle Eastern', 'icon': Icons.kebab_dining_rounded, 'color': Colors.purpleAccent},
    {'name': 'Italian', 'icon': Icons.local_pizza_rounded, 'color': DroniveryColors.electricOrange},
    {'name': 'Burgers', 'icon': Icons.fastfood_rounded, 'color': Colors.blueAccent},
  ];

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 48,
      child: ListView.separated(
        scrollDirection: Axis.horizontal,
        itemCount: categories.length,
        separatorBuilder: (_, __) => const SizedBox(width: 12),
        itemBuilder: (context, index) {
          final cat = categories[index];
          final name = cat['name'] as String;
          final isSelected = selectedCategory == name;
          final icon = cat['icon'] as IconData;

          return FilterChip(
            selected: isSelected,
            showCheckmark: false,
            avatar: Icon(icon, size: 16, color: isSelected ? Colors.white : DroniveryColors.darkSlate),
            label: Text(name),
            labelStyle: TextStyle(
              color: isSelected ? Colors.white : DroniveryColors.darkSlate,
              fontWeight: isSelected ? FontWeight.w900 : FontWeight.w600,
            ),
            selectedColor: DroniveryColors.emeraldTeal,
            backgroundColor: Colors.white,
            side: BorderSide(
              color: isSelected ? DroniveryColors.emeraldTeal : DroniveryColors.borderLight,
              width: 1.5,
            ),
            onSelected: (_) => onCategorySelected(name),
          );
        },
      ),
    );
  }
}

// ==========================================
// SCREEN 2: ABOUT US
// ==========================================

class AboutUsScreen extends StatelessWidget {
  const AboutUsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(28),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(32),
            decoration: BoxDecoration(
              gradient: const LinearGradient(
                colors: [Color(0xFF0F172A), Color(0xFF1E293B)],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
              borderRadius: BorderRadius.circular(24),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text(
                  'AUTONOMOUS SKYWAY LOGISTICS',
                  style: TextStyle(
                    color: DroniveryColors.emeraldTeal,
                    fontWeight: FontWeight.w900,
                    letterSpacing: 1.5,
                    fontSize: 12,
                  ),
                ),
                SizedBox(height: 8),
                Text(
                  'How Dronivery Air Fleet Operates',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 32,
                    fontWeight: FontWeight.w900,
                  ),
                ),
                SizedBox(height: 12),
                Text(
                  'Dronivery connects local kitchens to your doorstep using certified quad-rotor electric autonomous flight systems. Fast, zero emissions, and under 20 minutes.',
                  style: TextStyle(color: Color(0xFF94A3B8), fontSize: 15, height: 1.4),
                ),
              ],
            ),
          ),
          const SizedBox(height: 36),

          const Text(
            '3-Step Autonomous Delivery Flow',
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.w900, color: DroniveryColors.darkSlate),
          ),
          const SizedBox(height: 20),

          LayoutBuilder(
            builder: (context, constraints) {
              final isWide = constraints.maxWidth >= 900;
              if (isWide) {
                return Row(
                  children: const [
                    Expanded(
                      child: _StepCard(
                        stepNum: '01',
                        title: 'Kitchen Thermal Loading',
                        description:
                            'Kitchens seal your meal in an insulated thermal pod loaded directly into the drone payload bay.',
                        imageUrl: 'https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=800&auto=format&fit=crop',
                        icon: Icons.inventory_2_rounded,
                      ),
                    ),
                    SizedBox(width: 20),
                    Expanded(
                      child: _StepCard(
                        stepNum: '02',
                        title: 'Autonomous Skyway Flight',
                        description:
                            'AI navigation systems navigate designated air corridors at 200ft altitude at 65 MPH.',
                        imageUrl: 'https://images.unsplash.com/photo-1527977966376-1c8408f9f108?w=800&auto=format&fit=crop',
                        icon: Icons.flight_takeoff_rounded,
                      ),
                    ),
                    SizedBox(width: 20),
                    Expanded(
                      child: _StepCard(
                        stepNum: '03',
                        title: 'Precision Tether Drop',
                        description:
                            'Quad-rotors hover at 20 feet and lower your meal softly onto your lawn or delivery pad.',
                        imageUrl: 'https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=800&auto=format&fit=crop',
                        icon: Icons.file_download_rounded,
                      ),
                    ),
                  ],
                );
              }

              return Column(
                children: const [
                  _StepCard(
                    stepNum: '01',
                    title: 'Kitchen Thermal Loading',
                    description:
                        'Kitchens seal your meal in an insulated thermal pod loaded directly into the drone payload bay.',
                    imageUrl: 'https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=800&auto=format&fit=crop',
                    icon: Icons.inventory_2_rounded,
                  ),
                  SizedBox(height: 20),
                  _StepCard(
                    stepNum: '02',
                    title: 'Autonomous Skyway Flight',
                    description:
                        'AI navigation systems navigate designated air corridors at 200ft altitude at 65 MPH.',
                    imageUrl: 'https://images.unsplash.com/photo-1527977966376-1c8408f9f108?w=800&auto=format&fit=crop',
                    icon: Icons.flight_takeoff_rounded,
                  ),
                  SizedBox(height: 20),
                  _StepCard(
                    stepNum: '03',
                    title: 'Precision Tether Drop',
                    description:
                        'Quad-rotors hover at 20 feet and lower your meal softly onto your lawn or delivery pad.',
                    imageUrl: 'https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=800&auto=format&fit=crop',
                    icon: Icons.file_download_rounded,
                  ),
                ],
              );
            },
          ),
          const SizedBox(height: 36),

          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(28),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: DroniveryColors.borderLight),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  'Autonomous Fleet Performance Specs',
                  style: TextStyle(fontSize: 18, fontWeight: FontWeight.w900, color: DroniveryColors.darkSlate),
                ),
                const SizedBox(height: 20),
                Wrap(
                  spacing: 20,
                  runSpacing: 20,
                  children: const [
                    _SpecTile(title: 'Max Speed', value: '65 MPH', subtitle: 'Wind Resistant AI Flight'),
                    _SpecTile(title: 'Delivery Radius', value: '15 Miles', subtitle: '20 Miles for Gold Members'),
                    _SpecTile(title: 'Eco Footprint', value: '100% Electric', subtitle: 'Zero Carbon Footprint'),
                    _SpecTile(title: 'Safety Record', value: '99.99%', subtitle: 'Redundant Quad Motors'),
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _StepCard extends StatelessWidget {
  const _StepCard({
    required this.stepNum,
    required this.title,
    required this.description,
    required this.imageUrl,
    required this.icon,
  });

  final String stepNum;
  final String title;
  final String description;
  final String imageUrl;
  final IconData icon;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: DroniveryColors.borderLight),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.04),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            height: 180,
            child: Stack(
              children: [
                SafeNetworkImage(
                  imageUrl: imageUrl,
                  height: double.infinity,
                  width: double.infinity,
                  borderRadius: const BorderRadius.only(
                    topLeft: Radius.circular(20),
                    topRight: Radius.circular(20),
                  ),
                  fallbackIcon: icon,
                  fallbackTitle: title,
                ),
                Positioned(
                  top: 12,
                  left: 12,
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                    decoration: BoxDecoration(
                      color: DroniveryColors.emeraldTeal,
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: Text(
                      'STEP $stepNum',
                      style: const TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.w900,
                        fontSize: 12,
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: const TextStyle(
                    fontSize: 17,
                    fontWeight: FontWeight.w900,
                    color: DroniveryColors.darkSlate,
                  ),
                ),
                const SizedBox(height: 8),
                Text(
                  description,
                  style: const TextStyle(fontSize: 13, color: DroniveryColors.textSubtle, height: 1.4),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _SpecTile extends StatelessWidget {
  const _SpecTile({
    required this.title,
    required this.value,
    required this.subtitle,
  });

  final String title;
  final String value;
  final String subtitle;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 210,
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: DroniveryColors.sidebarTint,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: DroniveryColors.emeraldTeal.withOpacity(0.3)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(title, style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: DroniveryColors.textSubtle)),
          const SizedBox(height: 4),
          Text(
            value,
            style: const TextStyle(
              fontSize: 22,
              fontWeight: FontWeight.w900,
              color: DroniveryColors.emeraldTeal,
            ),
          ),
          const SizedBox(height: 2),
          Text(subtitle, style: const TextStyle(fontSize: 11, color: DroniveryColors.textSubtle)),
        ],
      ),
    );
  }
}

// ==========================================
// SCREEN 3: PROMO & DISCOUNT COUPONS
// ==========================================

class PromoScreen extends StatelessWidget {
  const PromoScreen({
    super.key,
    required this.isGoldMember,
    required this.onUpgradePressed,
    required this.onApplyPromoToCart,
  });

  final bool isGoldMember;
  final VoidCallback onUpgradePressed;
  final ValueChanged<String> onApplyPromoToCart;

  static const promos = [
    {
      'code': 'FIRSTFLY',
      'discount': '\$10 OFF',
      'title': 'First Flight Special',
      'subtitle': 'Valid on your first autonomous drone order of \$20 or more.',
      'tag': 'ALL USERS',
      'color': DroniveryColors.emeraldTeal,
    },
    {
      'code': 'DRONEFREE',
      'discount': 'FREE DELIVERY',
      'title': 'Zero Delivery Fee Coupon',
      'subtitle': 'Waives standard aerial dispatch fees on orders over \$25.',
      'tag': 'POPULAR',
      'color': DroniveryColors.electricOrange,
    },
    {
      'code': 'GOLDFLASH',
      'discount': '30% OFF',
      'title': 'Gold Member Exclusive',
      'subtitle': '30% discount on gourmet meals & dragon roll sushi platters.',
      'tag': 'GOLD MEMBERS',
      'color': DroniveryColors.warmSunset,
    },
    {
      'code': 'NIGHTOWL',
      'discount': '15% OFF',
      'title': 'Late Night Drone Flight',
      'subtitle': 'Applicable on air deliveries between 8:00 PM and 2:00 AM.',
      'tag': 'NIGHT FLIGHTS',
      'color': Colors.purpleAccent,
    },
  ];

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(28),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(32),
            decoration: BoxDecoration(
              gradient: const LinearGradient(
                colors: [Color(0xFF0F172A), Color(0xFF1E293B)],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
              borderRadius: BorderRadius.circular(24),
            ),
            child: Row(
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: const [
                      Text(
                        'DRONE PROMOTIONS & DISCOUNTS',
                        style: TextStyle(
                          color: DroniveryColors.emeraldTeal,
                          fontWeight: FontWeight.w900,
                          letterSpacing: 1.5,
                          fontSize: 12,
                        ),
                      ),
                      SizedBox(height: 8),
                      Text(
                        'Special Air Coupons',
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 30,
                          fontWeight: FontWeight.w900,
                        ),
                      ),
                      SizedBox(height: 8),
                      Text(
                        'Apply promo codes in cart checkout to save on flight delivery & food prices.',
                        style: TextStyle(color: Color(0xFF94A3B8), fontSize: 14),
                      ),
                    ],
                  ),
                ),
                const Icon(Icons.local_offer_rounded, size: 64, color: DroniveryColors.emeraldTeal),
              ],
            ),
          ),
          const SizedBox(height: 32),

          LayoutBuilder(
            builder: (context, constraints) {
              final crossAxisCount = constraints.maxWidth > 800 ? 2 : 1;
              return GridView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: promos.length,
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: crossAxisCount,
                  crossAxisSpacing: 20,
                  mainAxisSpacing: 20,
                  childAspectRatio: 2.1,
                ),
                itemBuilder: (context, index) {
                  final promo = promos[index];
                  final code = promo['code'] as String;

                  return Container(
                    padding: const EdgeInsets.all(22),
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(color: DroniveryColors.borderLight),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.04),
                          blurRadius: 10,
                          offset: const Offset(0, 4),
                        ),
                      ],
                    ),
                    child: Row(
                      children: [
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Row(
                                children: [
                                  Text(
                                    promo['discount'] as String,
                                    style: TextStyle(
                                      fontSize: 22,
                                      fontWeight: FontWeight.w900,
                                      color: promo['color'] as Color,
                                    ),
                                  ),
                                  const SizedBox(width: 8),
                                  Container(
                                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                                    decoration: BoxDecoration(
                                      color: (promo['color'] as Color).withOpacity(0.15),
                                      borderRadius: BorderRadius.circular(8),
                                    ),
                                    child: Text(
                                      promo['tag'] as String,
                                      style: TextStyle(
                                        color: promo['color'] as Color,
                                        fontSize: 9,
                                        fontWeight: FontWeight.w900,
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                              const SizedBox(height: 4),
                              Text(
                                promo['title'] as String,
                                style: const TextStyle(
                                  fontWeight: FontWeight.w900,
                                  fontSize: 15,
                                  color: DroniveryColors.darkSlate,
                                ),
                              ),
                              const SizedBox(height: 4),
                              Text(
                                promo['subtitle'] as String,
                                maxLines: 2,
                                overflow: TextOverflow.ellipsis,
                                style: const TextStyle(fontSize: 12, color: DroniveryColors.textSubtle),
                              ),
                            ],
                          ),
                        ),
                        const SizedBox(width: 12),
                        Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                              decoration: BoxDecoration(
                                color: DroniveryColors.sidebarTint,
                                borderRadius: BorderRadius.circular(10),
                                border: Border.all(color: DroniveryColors.emeraldTeal.withOpacity(0.3)),
                              ),
                              child: Text(
                                code,
                                style: const TextStyle(
                                  fontFamily: 'monospace',
                                  fontWeight: FontWeight.w900,
                                  fontSize: 14,
                                  color: DroniveryColors.deepEmerald,
                                ),
                              ),
                            ),
                            const SizedBox(height: 8),
                            ElevatedButton(
                              onPressed: () => onApplyPromoToCart(code),
                              style: ElevatedButton.styleFrom(
                                backgroundColor: DroniveryColors.emeraldTeal,
                                foregroundColor: Colors.white,
                                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
                                minimumSize: Size.zero,
                              ),
                              child: const Text('Apply Code', style: TextStyle(fontSize: 11, fontWeight: FontWeight.w900)),
                            ),
                          ],
                        ),
                      ],
                    ),
                  );
                },
              );
            },
          ),
        ],
      ),
    );
  }
}

// ==========================================
// SCREEN 4: PREMIUM ("DRONIVERY GOLD MEMBER")
// ==========================================

class GoldMemberScreen extends StatefulWidget {
  const GoldMemberScreen({
    super.key,
    required this.isGoldMember,
    required this.onToggleGold,
  });

  final bool isGoldMember;
  final VoidCallback onToggleGold;

  @override
  State<GoldMemberScreen> createState() => _GoldMemberScreenState();
}

class _GoldMemberScreenState extends State<GoldMemberScreen> {
  bool _isAnnual = false;

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(28),
      child: Center(
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxWidth: 850),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Container(
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: DroniveryColors.warmSunset.withOpacity(0.15),
                  shape: BoxShape.circle,
                ),
                child: const Icon(
                  Icons.workspace_premium_rounded,
                  size: 64,
                  color: DroniveryColors.warmSunset,
                ),
              ),
              const SizedBox(height: 16),

              const Text(
                'Dronivery Gold Member',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 34,
                  fontWeight: FontWeight.w900,
                  color: DroniveryColors.darkSlate,
                ),
              ),
              const SizedBox(height: 8),
              const Text(
                'Elevate your dining experience with priority autonomous sky routing, zero delivery fees, and extended range.',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 15, color: DroniveryColors.textSubtle),
              ),
              const SizedBox(height: 24),

              // Billing Selector Toggle
              Container(
                padding: const EdgeInsets.all(4),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(30),
                  border: Border.all(color: DroniveryColors.borderLight),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    GestureDetector(
                      onTap: () => setState(() => _isAnnual = false),
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                        decoration: BoxDecoration(
                          color: !_isAnnual ? DroniveryColors.darkSlate : Colors.transparent,
                          borderRadius: BorderRadius.circular(24),
                        ),
                        child: Text(
                          'Monthly (\$9.99/mo)',
                          style: TextStyle(
                            color: !_isAnnual ? Colors.white : DroniveryColors.darkSlate,
                            fontWeight: FontWeight.bold,
                            fontSize: 13,
                          ),
                        ),
                      ),
                    ),
                    GestureDetector(
                      onTap: () => setState(() => _isAnnual = true),
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                        decoration: BoxDecoration(
                          color: _isAnnual ? DroniveryColors.darkSlate : Colors.transparent,
                          borderRadius: BorderRadius.circular(24),
                        ),
                        child: Text(
                          'Annual (\$99/yr - Save 20%)',
                          style: TextStyle(
                            color: _isAnnual ? Colors.white : DroniveryColors.darkSlate,
                            fontWeight: FontWeight.bold,
                            fontSize: 13,
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 32),

              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(36),
                decoration: BoxDecoration(
                  gradient: const LinearGradient(
                    colors: [Color(0xFF0F172A), Color(0xFF1E293B)],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  borderRadius: BorderRadius.circular(28),
                  border: Border.all(color: DroniveryColors.warmSunset, width: 2),
                  boxShadow: [
                    BoxShadow(
                      color: DroniveryColors.warmSunset.withOpacity(0.25),
                      blurRadius: 24,
                      offset: const Offset(0, 8),
                    ),
                  ],
                ),
                child: Column(
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
                      decoration: BoxDecoration(
                        color: DroniveryColors.warmSunset,
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: const Text(
                        'RECOMMENDED FOR DRONE FOODIES',
                        style: TextStyle(color: Colors.black, fontSize: 11, fontWeight: FontWeight.w900),
                      ),
                    ),
                    const SizedBox(height: 20),

                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.baseline,
                      textBaseline: TextBaseline.alphabetic,
                      children: [
                        Text(
                          _isAnnual ? '\$99' : '\$9.99',
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 52,
                            fontWeight: FontWeight.w900,
                          ),
                        ),
                        const SizedBox(width: 6),
                        Text(
                          _isAnnual ? '/ year' : '/ month',
                          style: const TextStyle(color: Color(0xFF94A3B8), fontSize: 16, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    Text(
                      _isAnnual ? 'Equivalent to \$8.25/mo billed annually' : 'Or \$99 billed annually (Save 20%)',
                      style: const TextStyle(color: DroniveryColors.emeraldTeal, fontSize: 14, fontWeight: FontWeight.w900),
                    ),
                    const SizedBox(height: 28),

                    const Divider(color: Color(0xFF334155)),
                    const SizedBox(height: 24),

                    const _GoldPerkCheckTile(
                      title: 'Free Priority Drone Routing',
                      subtitle: 'Bypass peak flight queues & enjoy instant air dispatch.',
                    ),
                    const SizedBox(height: 16),
                    const _GoldPerkCheckTile(
                      title: 'Zero Delivery Fees',
                      subtitle: '\$0 delivery fee on all restaurant orders over \$15.',
                    ),
                    const SizedBox(height: 16),
                    const _GoldPerkCheckTile(
                      title: 'Extended 20-Mile Radius',
                      subtitle: 'Access distant specialty kitchens across the city.',
                    ),
                    const SizedBox(height: 16),
                    const _GoldPerkCheckTile(
                      title: 'Member-Only Flash Sales',
                      subtitle: 'Exclusive discounts on sushi, steaks, and gourmet meals.',
                    ),
                    const SizedBox(height: 16),
                    const _GoldPerkCheckTile(
                      title: 'Live 4K Payload Camera Stream',
                      subtitle: 'Watch your food fly real-time from takeoff to drop-off.',
                    ),

                    const SizedBox(height: 36),

                    SizedBox(
                      width: double.infinity,
                      height: 56,
                      child: ElevatedButton(
                        onPressed: widget.onToggleGold,
                        style: ElevatedButton.styleFrom(
                          backgroundColor: widget.isGoldMember ? Colors.white : DroniveryColors.warmSunset,
                          foregroundColor: Colors.black,
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(28)),
                          elevation: 0,
                        ),
                        child: Text(
                          widget.isGoldMember ? 'Manage / Cancel Gold Subscription' : (_isAnnual ? 'Upgrade Now - \$99/yr' : 'Upgrade Now - \$9.99/mo'),
                          style: const TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.w900,
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _GoldPerkCheckTile extends StatelessWidget {
  const _GoldPerkCheckTile({
    required this.title,
    required this.subtitle,
  });

  final String title;
  final String subtitle;

  @override
  Widget build(BuildContext context) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          padding: const EdgeInsets.all(4),
          decoration: const BoxDecoration(
            color: DroniveryColors.warmSunset,
            shape: BoxShape.circle,
          ),
          child: const Icon(Icons.check, size: 14, color: Colors.black),
        ),
        const SizedBox(width: 14),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                title,
                style: const TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 15,
                ),
              ),
              const SizedBox(height: 2),
              Text(
                subtitle,
                style: const TextStyle(color: Color(0xFF94A3B8), fontSize: 12),
              ),
            ],
          ),
        ),
      ],
    );
  }
}
'''

with open('/Users/adrian/StudioProjects/dronivery/lib/main.dart', 'w') as f:
    f.write(code)

print('Successfully generated complete main.dart!')

# Swiggy_automation
Browser Setup: Launches Chrome, maximizes the window, and navigates to Swiggy’s homepage.

Login: Waits for and clicks the “Sign In” button, enters a phone number into the login form, clicks to send the OTP, then pauses to allow manual OTP entry before continuing.

Post‑Login Confirmation: Prints the page title and URL to confirm successful login.

Search for “Dominos”: Opens the search box in the header, types “Dominos,” and submits the search. It retries for up to 30 seconds if the search elements aren’t immediately available.

Select Restaurant: Waits for the “Domino” result to become clickable and clicks it.

Add Item to Cart: Scrolls to and clicks the first “Add” button for a menu item, then clicks “View Cart.”

Enter Address: Clicks “Add New Address,” waits for you to manually enter the address, then clicks “Save Address.”

Proceed to Payment: Clicks the “Proceed to Payment” button in the cart.

Completion: Prints a final message indicating that automation is complete and prompts you to review the cart and payment page manually.

Throughout, it uses explicit waits (WebDriverWait) to handle dynamic loading, and takes screenshots if key elements fail to appear.

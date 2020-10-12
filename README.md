**DISCLAIMER: This project is for educational purposes only, no materials/files are intended for any commercial use. In this document all sources will be credited.**

- [Milestone 4 - The Woodworks](#milestone-4---the-woodworks)
    + [The journey of developing The Woodworks (this can be seen by working through the commit history).](#the-journey-of-developing-the-woodworks--this-can-be-seen-by-working-through-the-commit-history-)
  * [UX](#ux)
    + [User stories](#user-stories)
    + [Model design](#model-design)
      - [Product](#product)
      - [Reviews](#reviews)
      - [Poll](#poll)
    + [Color scheme](#color-scheme)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>




# Milestone 4 - The Woodworks

The milestone 4 project will be a website to showcase content I learned to develop in the last part of the Code Institute's Full stack developer bootcamp. It will be a Django based full stack website. Since I am on an extremely tight schedule I will build a minimal viable product first and expand on that if time permits. 

I chose to build a small e-commerce site for a dear friend of mine who will be starting a training in furniture woodworking and might be selling his creations in the future. The site I will build is a showcase to see how it might work.

As I have been working through the course material I experienced a big overload of information, so I needed to start building my project. In my past experience I found that worked a lot better than just working through the course material. Because of the sheer size of the possibities I will not be designing the whole site beforehand. General mockups and the look and feel can be designed early in the process, but all functionality and features will be chosen and developed as I go along.

### The journey of developing The Woodworks
I started development using very simple apps to push through the content fast so I could get the major roadblocks out of the way. I needed to be sure that I had the site working before complicating everything with styling, more products, etc. So with this in mind I build the apps and views (store, cart and add to cart functionality) necessary to get to the checkout page, then to the checkout itself and succesfull payment functionality using stripe. Orders were being entered into the database as well at this point. I also switched quite early to having my mediafiles being pulled from AWS S3 instead of local content, to be sure that was working as well. With all that finished I did an early deployement to heroku.

After that I went and build up the site for real, adding the review app, the poll app and all styling and true layout. Adding more items to be sold, some items for the poll and some sample reviews. Adding more styling and some Javascript to spice things up.

## UX

The following features need to be present at a minimum:

- The site needs to be clear and responsive.
- A landing page which will display purchaseable products
- A navbar including a shopping cart and a way to differentiate between a logged on/off user.
- A way to add products to the shopping cart.
- A login system using e-mail confirmation.
- Two additional apps not used in the Boutique Ado mini-project of the course material:
  1. A review page where each product can be reviewed.
  2. Either a contact form, or a page with a poll on what furniture product to develop next.
- A checkout page with fields for an address to send the product(s) to.
- A working payment system using Stripe and it's testing facilities.

### User stories

As a user that is not logged in:
- I want to view products on offer
- I want to look at reviews
- I want to look at the poll for the next product to be developed.
- I want to register for a new account
- I want login if I already have an account
- I want to add a product to my shopping cart
- I want to be able to see the contents of my shopping cart and adjust it if necessary.

As a user that is logged in:
- I want to add a review to a product
- I want to add a product to my shopping cart
- I want to see the contents of my shopping cart
- I want to checkout my purchases and pay for them
- I want to vote for the next product to be developed.

### Model design

#### Product
The products model will be several types of furniture, in the database design the model will have the following fields:
- product_id (primary key)
- name (string)
- description (string)
- price (integer)
- construction time (integer representing weeks)
- image (file)

#### Reviews
The review model will add reviews to products and use product_id as a foreign key.
- review_id (primary key)
- product_id (foreign key)
- review_text (string)

#### Poll
The poll model will contain a product type and votes cast per type. Time permitting it will be linked to a user account so a user can only vote once.
- product_type_id
- product_type (string)
- votes (integer)

A seperate model for the poll app was implemented during development will be present to keep track of who has voted. These are identified by their emaildres.
- Voters/voted (contains only emailadresses)

The database model can be viewed [here](https://github.com/codewouter/milestone4-the-woodworks/blob/master/mockups/ms4-db-model.pdf):

### Color scheme

Using https://coolors.co/ I picked a scheme that had a lot of green in it and some nice contrast giving it a bit of a 'nature' feel.

![Colorscheme image](https://ms4-the-woodworks.s3.eu-west-2.amazonaws.com/media/images/Colorpalette500x.png)

Colors from left to right:
- 606C38
- 283618
- FEFAE0
- DDA15E
- BC6C25

### Naming scheme

- HTML/CSS: using dashes, eg. toggle-info-button
- Javascript: camelcase, eg. toggleElementView
- Python: underscores. eg. view_reviews

### Planned pages

- Login/ registration page
    * Self explanetory. Will be provided by Django's allauth app. Some sytling might be necessary.

**Pages for the flow of shopping. Selecting, ordering, checkout, payment, confirmation.**

- Landing/store page
    * The landing is page will also be the store page. The site will contain the products that can be purchased. Here they can be added to the shopping cart. A maximum of 5 items each to keep users from ordering 100's of items. It will contain a button to go to the reviews section of the relevant product. Details of the product will be:
    * picture of product
        * name
        * description (should be hidden on mobile, with an option to show it (button))
        * price
        * construction time

- Shopping cart page
    * This page will give an overview of the contents of the shopping cart, including total price and construtcion time. Here the user can adjust the cart's content and ultimately got to checkout. To go to checkout the user needs to be logged in.

- Checkout page
    * The checkout page will only show if the user is logged on. Here the user is shown a condensed view of the carts contents and the grand total to be payout. A form to fill out all the user's details, including payment details, is loaded. After that the user is given an option (button) to complete the order.

- Checkout succes page
    * A simple page to show that the order has followed through. If time permits it will show the order, payment and send an email for confirmation.

**Other pages**
- Review page
    * A page that will show reviews entered by users for a product. If logged in, the user can add reviews.

- Poll page
    * A poll will be shown here that asks to vote on the product to be developed next by the woodworks. If logged on the user can vote, if not, the user can view the results up to now.

Mockups of several of the pages can be viewed [here](https://github.com/codewouter/milestone4-the-woodworks/blob/master/mockups/the-woodworkds-mockups.pdf)

I have not made mockups of all pages as some were developed 'on the fly' during developement. As mentioned earlier, I went with exremely simplistic design to get all the way to a working deployed site. When that was finished I started polishing what was there and never felt I needed to build mockups first. The general design of the site was quite clear from the mockups I did make.

## Features

### Existing Features

#### Consistent features across all pages
- A navbar to navigate around the site. The links for Store, Vote and Cart are always present. When logged in there is a logout option. If not, links for register and login are present. The cart has a small addition showing the number of products in the cart if any are present. On the left the name of the shop is present and acts as a 'home' link. On small viewports all links will be replaced with a hamburger menu which will slide open to reveal all links.
- A simple footer to indicate the bottom of the page, containing a copyright mark.

#### Store / Landing page
- As per design these are one and the same.


### Defensive design







On stripe:

Got stripe running, payments are created and accepted, webhooks are being handled. Creating the whole customer data passing and so on, simply takes too much time and will be left out. Test webhooks send from Stripe are being handled and returned with a proper response.


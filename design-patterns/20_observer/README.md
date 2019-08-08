# Observer Design pattern
 - Also known as Publish-Subscribe
 - It's behavioral design pattern
 
##Definition as per GoF
 - Define a one-to-many dependency between Objects so that when one object changes state, all it's dependencyare notified and updated automatically
 
 
## UML Diagram

  ![Screenshot](doc/images/1.png)
  
##Advantages
 - Provides a loosely coupled design between objects that interact
 - Observer pattern provides this loose coupling as:

      - Subject only knows that observer implement Observer interface.Nothing more.
      - There is no need to modify Subject to add or remove observers.
      - We can reuse subject and observer classes independently of each other.
      
 - Support for broadcast communication
##Disadvantages
 - Memory leaks caused by Lapsed listener problem because of explicit register and unregistering of observers.
 
## Known Usage
 - It is heavily used in GUI toolkits and event listener. 
 
      - In java the button(subject) and onClickListener(observer) are modelled with observer pattern.
      
     
 - Social media, RSS feeds, email subscription in which you have the option to follow or subscribe and you receive latest notification.
 - All users of an app on play store gets notified if there is an update.
 
## Example UML-

   ![Screenshot](doc/images/CricketAppObserver.png)

 
 
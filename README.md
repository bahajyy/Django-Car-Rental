# Se3355FinalProject

Projeyi ve deploymentı gösterdiğim video linki:
(Azure para çektiği için videodan sonra deployment ve webappi kaldırıyorum)
https://www.youtube.com/watch?v=kAD9Yg2zwQI


The Django project aims to create a comprehensive car rental system with three primary models: UserProfile, Car, and Client. The built-in User model is utilized for user authentication, while the Client model extends the user profile, incorporating additional details such as country and city. This one-to-one relationship between a user and a client ensures a seamless integration of user-specific information.

The UserProfile model serves as a repository for user-related data, encompassing fields like email, password, country, and city. The model's __str__ method enhances its representation by returning the user's email.

The Car model embodies the attributes of available rental cars, encompassing brand, model, city, transmission type, deposit amount, mileage, age, cost of rental, available start date, and available end date. The transmission type field benefits from predefined choices, optimizing data consistency.

The Client model acts as an extension to the user profile, appending details specifically relevant to the car rental service, notably, country and city. This model maintains a one-to-one relationship with the built-in User model, and its __str__ method ensures a meaningful representation by returning the associated user's username.


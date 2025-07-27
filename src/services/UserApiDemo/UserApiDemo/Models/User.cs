namespace UserApiDemo.Models;
public class User
{ 
        public int Id { get; set; }
        public string Name { get; set; } = string.Empty;
        public string Email { get; set; } = string.Empty; // "1" => string; 1 => int/long

        public UserResponse<string> ResponseName()
        {
                return new UserResponse<string>()
                {
                        Response = Name
                };
        }
        
        public UserResponse<string> ResponseEmail()
        {
                return new UserResponse<string>()
                {
                        Response = Email
                };
        }
        
        public UserResponse<int> ResponseId()
        {
                return new UserResponse<int>()
                {
                        Response = Id
                };
        }
        
        public UserResponse<User> ResponseUser()
        {
                return new UserResponse<User>()
                {
                        Response = new User()
                        {
                                Id = Id,
                                Name = Name,
                                Email = Email
                        }
                };
        }
}

public class UserResponse<T> where T : notnull
{
        public T Response { get; set; } = default!;

        public string GetTypeName()
        {
                return Response.GetType().Name; // "Dog", int -> "int", string -> "string"
        }
}
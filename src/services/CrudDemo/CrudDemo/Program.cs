using System;
using System.Linq;
using CrudDemo; 

class Program
{
    static void Main()
    {
        using var context = new AppDbContexts();

        // CREATE
        context.Students.Add(new Student { Name = "John Doe", Age = 20 });
        context.SaveChanges();

        // READ
        var students = context.Students.ToList();
        foreach (var s in students)
            Console.WriteLine($"{s.Id} - {s.Name}, {s.Age} tuổi");

        // UPDATE
        var student = context.Students.First();
        student.Name = "Jane Doe";
        context.SaveChanges();

        // DELETE
        context.Students.Remove(student);
        context.SaveChanges();
    }
}


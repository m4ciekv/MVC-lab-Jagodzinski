using Microsoft.AspNetCore.Mvc;
using MvcMovie.Models;

namespace MvcMovie.Controllers;

public class HelloWorldController : Controller
{
    public string Index()
    {
        return "This is my default action...";
    }

    public IActionResult Welcome(string name, int numTimes = 1)
    {
        var model = new HelloWorldModel
        {
            Name = name,
            NumTimes = numTimes
        };

        return View(model);
    }
}
using System.Threading.Tasks;
using Microsoft.AspNetCore.SignalR;

namespace Alfred.Hubs
{
    public class PassthroughHub : Hub
    {
        public async Task SendMessage(string user, string message)
        {
            await Clients.All.SendAsync("ReceiveMessage", user, message);
        }
    }
}
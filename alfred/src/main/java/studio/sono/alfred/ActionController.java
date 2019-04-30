package studio.sono.alfred;

import org.springframework.messaging.handler.annotation.DestinationVariable;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.stereotype.Controller;

@Controller
public class ActionController {
    @MessageMapping("/action/{projectId}")
    @SendTo("/action/{projectId}")
    public String action(@DestinationVariable String projectId, String message) {
        System.out.println("Test");
        return message;
    }
}

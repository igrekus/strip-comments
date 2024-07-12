from strip_comments import strip

source = '''Ada
The Ada programming language uses '--' to indicate a comment up to the end of the line.

For example:

  -- the air traffic controller task takes requests for takeoff and landing
   task type Controller (My_Runway: Runway_Access) is
      -- task entries for synchronous message passing
      entry Request_Takeoff (ID: in Airplane_ID; Takeoff: out Runway_Access);
      entry Request_Approach(ID: in Airplane_ID; Approach: out Runway_Access);
   end Controller;
'''

expected = '''Ada
The Ada programming language uses '--' to indicate a comment up to the end of the line.

For example:

  
   task type Controller (My_Runway: Runway_Access) is
      
      entry Request_Takeoff (ID: in Airplane_ID; Takeoff: out Runway_Access);
      entry Request_Approach(ID: in Airplane_ID; Approach: out Runway_Access);
   end Controller;
'''


def test_strips_ada():
    assert strip.strip(source, language='ada', preserve_newlines=True) == expected

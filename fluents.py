def swapLastOcc(string_to_search,target,substitute):
    pos = string_to_search.rfind(target)
    if pos != -1:
        string_to_search = string_to_search[:pos] + substitute + string_to_search[pos+1:]
    return string_to_search
        
def check_fluent_conflicts(Fluents, conflicting_set_for_fluents):
    conflicting_fluents = {}
    for fluent in Fluents:
        starting_event = Fluents[fluent][0]
        end_events = Fluents[fluent][1]
        
        all_events = list(end_events)
        all_events.append(starting_event)
        
        for event in all_events:
            for conflict in conflicting_set_for_fluents:
                if event == conflict[1]:
                    if fluent not in conflicting_fluents:
                        conflicting_fluents[fluent] = set()
                    conflicting_fluents[fluent].add(event)
    conflicting_rules_set = set()
    for conflict in conflicting_set_for_fluents:
        conflicting_rules_set.add(conflict[0])

    #Build the strings for the output
    if(len(conflicting_fluents) >1):
        conflicting_rules_string = ','.join(conflicting_rules_set)
        conflicting_rules_string = swapLastOcc(conflicting_rules_string, ",", " and ")
        traced_fluents_string = ",".join(str(s) for s in conflicting_fluents)
        traced_fluents_string = swapLastOcc(traced_fluents_string, ",", " and ")
        return f"The conflict for {conflicting_rules_string} can be traced back to conflicts between goal fluents {traced_fluents_string}, which contain the initiating or terminating events involved.\n"
    return ""
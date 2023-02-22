from floodsystem.station import MonitoringStation

def sample_stations():
    """Creates a list of stations for test. All are valid
    s1 and s2 have been given valid latest levels"""
    s_id = "http://environment.data.gov.uk/flood-monitoring/id/stations/1029TH"
    m_id = "http://environment.data.gov.uk/flood-monitoring/id/measures/1029TH-level-stage-i-15_min-mASD"
    label = "Bourton Dickler"
    coord = (51.874767, -1.740083)
    trange = (0.068, 0.42)
    river = "River Dikler"
    town = "Little Rissington"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s1.latest_level = 0.3
    
    
    s_id2 = "http://environment.data.gov.uk/flood-monitoring/id/stations/E2043"
    m_id2 = "http://environment.data.gov.uk/flood-monitoring/id/measures/E2043-level-stage-i-15_min-mASD"
    label2 = "Surfleet Sluice"
    coord2 = (52.845991, -0.100848)
    trange2 = (0.15, 0.895)
    river2 = "River Glen"
    town2 = "Surfleet Seas End"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
    s2.latest_level = 0.7

    s_id3 = "http://environment.data.gov.uk/flood-monitoring/id/stations/52119"
    m_id3 = "http://environment.data.gov.uk/flood-monitoring/id/measures/52119-level-stage-i-15_min-mASD"
    label3 = "Gaw Bridge"
    coord3 = (50.976043, -2.793549)
    trange3 = (0.231, 2.8)
    river3 = "River Parrett"
    town3 = "Kingsbury Episcopi"
    s3 = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)

    s_id4 = "test-s-id"
    m_id4 = "test-m-id"
    label4 = "Kates Bridge"
    coord4 = (50.976043, -2.793549)
    trange4 = (0.231, 2.8)
    river4 = "River Glen"
    town4 = "My Town"
    s4 = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)

    return [s1,s2,s3,s4]

def create_invalid_typical_range_stations() -> list[MonitoringStation]:
    """Creates a list containing 2 stations with invalid ranges"""
    # Create a station with inconsistent level data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (10,0)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, None, river, town)
    return [s1, s2]

def create_invalid_relative_level_stations() -> list[MonitoringStation]:
    """Creates a list containing stations where the relative range method should return None"""
    s_id = ["test-s-id1", "test-s-id2", "test-s-id3"]
    m_id = ["test-m-id1", "test-m-id2", "test-m-id3"]
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (0,10)
    river = "River X"
    town = "My Town"
    level = 5
    station1 = MonitoringStation(s_id[0], m_id[0], label, coord, None, river, town)
    station1.latest_level = level
    station2 = MonitoringStation(s_id[1], m_id[1], label, coord, (5,5), river, town)
    station2.latest_level = level
    station3 = MonitoringStation(s_id[2], m_id[2], label, coord, trange, river, town) # no latest level
    return [station1, station2, station3]

def create_stations_level_over_threshold_data():
    """Creates a list containing stations for testing stations_level_over_threshold
    gaw and kates bridge should be the only ones over the threshold"""
    stations = sample_stations()
    stations += create_invalid_relative_level_stations()
    stations[2].latest_level = 2.8
    stations[3].latest_level = 2.7
    return stations



if __name__ == "__main__":
    print(sample_stations())
    print(create_invalid_typical_range_stations())
    print(create_invalid_relative_level_stations())
    print(create_stations_level_over_threshold_data())

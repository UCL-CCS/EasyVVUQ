import easyvvuq as uq
import os

__copyright__ = """

    Copyright 2018 Robin A. Richardson, David W. Wright 

    This file is part of EasyVVUQ 

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__license__ = "LGPL"


def test_campaign_dir_prefix(tmpdir):

    # Test inputs
    input_json = "tests/cannonsim/test_input/test_cannonsim_csv.json"
    output_json = os.path.join(tmpdir, "out_campaign_dir_prefix.json")
    alternative_prefix = "ALTERNATIVEPREFIX"
    
    assert( os.path.exists(input_json) )

    # Build a campaign with an alternative default prefix
    my_campaign = uq.Campaign(state_filename=input_json, workdir=tmpdir, default_campaign_dir_prefix=alternative_prefix)

    assert( my_campaign is not None )
    assert( len(my_campaign.campaign_ID()) > 0 )
    assert( my_campaign.campaign_ID().startswith(alternative_prefix) )
    assert( my_campaign.campaign_ID(without_prefix=True).startswith(alternative_prefix) == False )
    assert( len(my_campaign.campaign_ID(without_prefix=True)) > 0 )
    assert( 'campaign_dir_prefix' in my_campaign.app_info )
    assert( my_campaign.app_info['campaign_dir_prefix'] == alternative_prefix )
 
    # Save state of campaign
    my_campaign.save_state(output_json)

    assert( os.path.exists(output_json) )
    assert( os.path.isfile(output_json) )

    # Reload the campaign
    my_campaign = None
    reloaded_campaign = uq.Campaign(state_filename=output_json)

    assert( len(reloaded_campaign.campaign_ID()) > 0 )
    assert( reloaded_campaign.campaign_ID().startswith(alternative_prefix) )
    assert( reloaded_campaign.campaign_ID(without_prefix=True).startswith(alternative_prefix) == False )
    assert( len(reloaded_campaign.campaign_ID(without_prefix=True)) > 0 )
    assert( 'campaign_dir_prefix' in reloaded_campaign.app_info )
    assert( reloaded_campaign.app_info['campaign_dir_prefix'] == alternative_prefix )

if __name__ == "__main__":
    test_campaign_dir_prefix("/tmp/")
